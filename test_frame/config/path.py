import os
path=os.path.abspath(__file__)
config_path=os.path.dirname(path)
# 根目录路径
test_frame_path=os.path.dirname(config_path)
# reports路径
reports_path=os.path.join(test_frame_path,'reports')
# print(reports_path)
if not os.path.exists(reports_path):
    os.mkdir(reports_path)
#log路径
logs_path=os.path.join(test_frame_path,'logs')
if not os.path.exists(logs_path):
    os.mkdir(logs_path)
# excel路径
excel_path=os.path.join(test_frame_path,'data')
if not os.path.exists(excel_path):
    os.mkdir(excel_path)
