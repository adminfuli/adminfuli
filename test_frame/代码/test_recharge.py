from decimal import Decimal
from test_frame.middleware.middleware_data import Middleware
import requests
import pytest
import json
excel_data=Middleware().excel.read('recharge')
from test_frame.common.yaml_handler import yaml_config
@pytest.mark.parametrize('recharge_info',excel_data)
def test_recharge(recharge_info,login):
    member_id=recharge_info['json']
    # 替换id
    if "#member_id#" in member_id:
        member_id=member_id.replace("#member_id#",str(login['id']))
    # 替换token
    token = recharge_info['headers']
    if "token" in token:
        token=token.replace("token",login['all_token'])
    if "#wrong_id#" in member_id:
        member_id=member_id.replace("#wrong_id#",str(login['id']+1)) 
    # 之前的余额
    amount_before=Decimal(login["leave_amount"])
    url = ''.join([yaml_config['host'], recharge_info['url']])
    print(url)
    response=requests.request(method=recharge_info['method'],
                              url=''.join([yaml_config['host'],recharge_info['url']]),
                              json=json.loads(member_id),
                              headers=json.loads(token))
    response_data=response.json()
    # 充值之后的余额
    amount_after=Middleware.db_handler.query(one=False, sql='select leave_amount from member where id={}'.format(login['id']))
    amount_after=amount_after[0]['leave_amount']
    try:
        assert response_data['code']==recharge_info['expected']
    except AssertionError as a:
        Middleware.logger.info('断言失败{}'.format(a))
        raise a
    # 充值金额的提取
    if response_data['code']==0:
        amount=Decimal(str(eval(recharge_info['json'])['amount']))
        print(amount)
        assert amount_before + amount == amount_after
        # try:
        #     assert amount_before+amount==amount_after
        # except AssertionError as a:
        #     loggs.info('断言失败{}'.format(a))



