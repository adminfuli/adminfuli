from faker import Faker
from test_frame.common.db_handler import Db_handler
from test_frame.middleware.middleware_data import Middleware
import random


def generate_new_phone():
    fk=Faker(locale='zh_CN')
    while True:
        phone = fk.phone_number()
        db_handler_data =Middleware().db_handler.query(one=True, sql='select * from member where mobile_phone={} limit 10'.format(phone))
        Middleware().db_handler.close()
        if  not  db_handler_data:
            return phone
if __name__=='__main__':
    generate_new_phone=generate_new_phone()
    print(generate_new_phone)
# class Random_phone():
#     def __init__(self):
#         new_phone='1'+random.choice(['3','5','7','8','9'])
#         for i in range(9):
#             num=random.randint(0,9)
#             phone += str(num)
#         return phone
# random_phone=Random_phone()
# print(random_phone)