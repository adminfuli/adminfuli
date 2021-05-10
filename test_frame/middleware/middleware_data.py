from faker import Faker
import re

from test_frame.common.log_handler import my_logger
from test_frame.common.yaml_handler import yaml_config,yaml_secert_config
# log
import os
from test_frame.config import path
from test_frame.common.db_handler import Db_handler
from test_frame.common.excel_handler import Excel_handler
from test_frame.config.path import excel_path



class Middleware():
    # log
    file_name_path=os.path.join(path.logs_path,yaml_config['log']['file_name'])
    logger=my_logger(file_name=file_name_path,
                     name=yaml_config['log']['name'],
                     logger_level=yaml_config['log']['logger_level'],
                     hand_level=yaml_config['log']['hand_level'],
                     matter=yaml_config['log']['matter'],
                     file_level=yaml_config['log']['file_level'])
#    db
    db_handler = Db_handler(host=yaml_config['db']['host'],
                            user=yaml_config['db']['user'],
                            password=yaml_config['db']['password'],
                            database=yaml_config['db']['database'])
#     excel
    excel_login_path = os.path.join(excel_path, 'test_case.xlsx')
    excel = Excel_handler(excel_login_path)
#     help
    @staticmethod
    def generate_new_phone():
        fk = Faker(locale='zh_CN')
        while True:
            phone = fk.phone_number()
            db_handler_data = Middleware().db_handler.query(one=True,
                                                            sql='select * from member where mobile_phone={} limit 10'.format(
                                                                phone))
            Middleware().db_handler.close()
            if not db_handler_data:
                return phone
#     数据替换
    invest_phone=yaml_secert_config['invest']['invest_phone']
    invest_pwd=yaml_secert_config['invest']['invest_pwd']
    loan_phone=yaml_secert_config['loan']['loan_phone']
    loan_pwd=yaml_secert_config['loan']['loan_pwd']
    admin_phone=yaml_secert_config['admin']['admin_user']
    admin_pwd=yaml_secert_config['admin']['admin_pwd']
    @classmethod
    def replace_data(cls,string):
        pattern='#(.*?)#'
        re_data=re.finditer(pattern=pattern,string=string)
        for re_datas in re_data:
            old=re_datas.group()
            key=re_datas.group(1)
            new=str(getattr(cls,key,''))
            string=string.replace(old,new)
        return string
if __name__ == '__main__':
    # data=Middleware.db_handler.query(one=False,sql='select leave_amount from member where id=1000337779')
    print(Middleware.replace_data('{"mobile_phone": "#invest_phone#","pwd": "#invest_pwd#"}'))
    print(Middleware.invest_phone)



