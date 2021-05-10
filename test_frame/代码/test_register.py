import pytest
import requests
import json
from test_frame.middleware.middleware_data import Middleware
from test_frame.common.yaml_handler import yaml_config
excel_data=Middleware.excel.read('register')
@pytest.mark.parametrize('test_info',excel_data)
def test_register(test_info):
    actual_json = test_info['json']
    if "#phone#" in test_info['json']:
        actual_json = actual_json.replace("#phone#", Middleware.generate_new_phone())
    response=requests.request(method=test_info['method'],
                              url=yaml_config['host']+test_info['url'],
                              headers=eval(test_info['headers']),
                              json=eval(actual_json))
    res_body= response.json()
    expected=json.loads(test_info['excepted'])
    print(expected)

    for key,value in expected.items():
        try:
            assert res_body[key]==value
        except AssertionError as e:
            Middleware.logger.info('用例失败{}'.format(e))
            raise e

    # try:
    #     assert res_body['code']==test_info['excepted']
    # except AssertionError as e:
    #     Middleware.logger.info('用例失败{}'.format(e))
    #     raise e




