import pytest
import requests
import json
from test_frame.middleware.middleware_data import Middleware
from test_frame.common.yaml_handler import yaml_config
audit_data=Middleware.excel.read('audit')
@pytest.mark.parametrize('audit_info',audit_data)
def test_audit(audit_info,admin_login,add_loan):
    json_data = audit_info['json']
    if "#loan_id#" in json_data:
        json_data=json_data.replace("#loan_id#",str(add_loan['id']))
    token=audit_info['headers']
    if "token" in token:
        token=token.replace("token",admin_login["all_token"])
    response=requests.request(url=(yaml_config['host']+audit_info['url']),
                     method=audit_info['method'],
                     json=json.loads(json_data),
                     headers=json.loads(token))
    response_data=response.json()


    expect=json.loads(audit_info['expected'])
    for key,value in expect.items():
        assert value==response_data[key]



