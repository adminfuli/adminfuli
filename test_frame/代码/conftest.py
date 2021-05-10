import requests
from jsonpath import jsonpath
import pytest
from test_frame.common.yaml_handler import yaml_handler
from test_frame.common.yaml_handler import yaml_secert_config,yaml_config
# http://8.129.91.152:8766/futureloan/member/login
def login_fuc(phone,pwd):
    phone = phone
    pwd = pwd
    json_data = {"mobile_phone": phone, "pwd": pwd}
    reponse = requests.request(method='post',
                               url=yaml_config['host'] + '/member/login',
                               json=json_data,
                               headers={"X-Lemonban-Media-Type": "lemonban.v2"})
    response_data = reponse.json()
    id = jsonpath(response_data, '$..id')[0]
    token = jsonpath(response_data, '$..token')[0]
    token_type = jsonpath(response_data, '$..token_type')[0]
    all_token = " ".join([token_type, token])
    leave_amount = jsonpath(response_data, '$..leave_amount')[0]
    res_want = {"id": id, "all_token": all_token, "leave_amount": leave_amount}
    return res_want

@pytest.fixture()
def login():
    phone=yaml_secert_config['secret']['user']
    pwd=yaml_secert_config['secret']['pwd']
    return login_fuc(phone,pwd)
@pytest.fixture()
def admin_login():
    phone = yaml_secert_config['admin']['admin_user']
    pwd = yaml_secert_config['admin']['admin_pwd']
    return login_fuc(phone, pwd)
@pytest.fixture()
def add_loan(login):
    token=login['all_token']
    token_data={'X-Lemonban-Media-Type':'lemonban.v2','Authorization':token}
    json={"member_id":login['id'],
          "title":"自动化测试",
          "amount":6300.00,
          "loan_rate":12.0,
          "loan_term":12,
          "loan_date_type":1,
          "bidding_days":5}
    response=requests.request(method='post',
                     url=yaml_config['host'] + '/loan/add',
                     json=json,
                     headers=token_data)
    response_data=response.json()
    loan_id=jsonpath(response_data,'$..id')[0]
    res_want={'id':loan_id}
    return res_want

