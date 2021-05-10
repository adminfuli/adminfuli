import pytest
import os
from test_frame.config import path
from datetime import datetime
#获取当前时间
now_time=datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
print(now_time)
# 将时间写入到名字中
report_file_name='report'+now_time+'.html'
# 获取测试报告的目录
report_abs=path.reports_path
# 拼接文件
report_file=os.path.join(report_abs,report_file_name)

pytest.main(['--html={}'.format(report_file),'-s'])