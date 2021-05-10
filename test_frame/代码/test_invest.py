import json

import pytest
import requests
from jsonpath import jsonpath

from test_frame.common.yaml_handler import yaml_config
from test_frame.middleware.middleware_data import Middleware
invest_data=Middleware.excel.read('invest')
invest_data=invest_data
@pytest.mark.parametrize('invest_info',invest_data)
def test_invest(invest_info):
    # json_invest_data = json.dumps(invest_info)
    # my_str = Middleware.replace_data(invest_info)
    # new_my_str = json.loads(my_str)
    all_data=json.dumps(invest_info)
    json_data=Middleware.replace_data(all_data)
    use_data=json.loads(json_data)
    headers=use_data['headers']
    response=requests.request(method=use_data['method'],
                              url=yaml_config['host']+use_data['url'],
                              headers=eval(headers),
                              json=json.loads(use_data['json']))
    response_data=response.json()
    assert response_data['code']==invest_info['expected']
    if invest_info['response']:
        response_after = json.loads(invest_info['response'])
        for key, ex_value in response_after.items():
            want_value = jsonpath(response_data, ex_value)[0]
            setattr(Middleware, key, want_value)

