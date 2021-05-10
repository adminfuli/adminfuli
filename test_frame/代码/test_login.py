import pytest
import requests
from test_frame.middleware.middleware_data import Middleware
excel_data=Middleware.excel.read('login')
from test_frame.common.yaml_handler import yaml_config,yaml_secert_config


@pytest.mark.parametrize('login_info',excel_data)
def test_login(login_info):
    new_phone=login_info['json']
    if '#phone#' in new_phone:
        new_phone=new_phone.replace('#phone#',Middleware.generate_new_phone())
        print(new_phone)
    if '*user_phone*' in new_phone:
        new_phone=new_phone.replace('*user_phone*',yaml_secert_config['secret']['user'])
    if '*user_pwd*' in new_phone:
        new_phone=new_phone.replace('*user_pwd*',yaml_secert_config['secret']['pwd'])


    reponse_body=requests.request(url=yaml_config['host']+login_info['url'],
                     method=login_info['method'],
                     json=eval(new_phone),
                     headers=eval(login_info['headers']))
    reponse_data=reponse_body.json()
    try:
        assert reponse_data['code']==login_info['excepted']
    except AssertionError as e:
        Middleware.logger.loggs.info('用例失败{}'.format(e))
        raise e
