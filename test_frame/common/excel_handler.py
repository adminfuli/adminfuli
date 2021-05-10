import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
from pprint import pprint
class Excel_handler():
    def __init__(self,fpath):
        self.fpath=fpath

 #   print(list(data))

    def read(self,sheetname):

        wookbook = openpyxl.open(self.fpath)
        wooksheet = wookbook[sheetname]
        data = list(wooksheet.values)
        all_data=[]
        key=data[0]
        for row in data[1:]:
            row_dict=dict(zip(key,row))
            all_data.append(row_dict)
        wookbook.close()
        return all_data

if __name__=='__main__':
    excel_handler=Excel_handler('test_case.xlsx')
    excel_data=excel_handler.read('login')
    pprint(excel_data)

