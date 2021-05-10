# import logging
# import time
# from logging.handlers import RotatingFileHandler
# logger=logging.getLogger('PY36')
# handler=RotatingFileHandler('py3611.log',maxBytes=100,backupCount=3,encoding='utf-8')
# logger.addHandler(handler)
# for i in range(100):
#     logger.warning('测试调试{}'.format(time.time()))
#     time.sleep(0.1)
import logging
import time
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler
logger=logging.getLogger('PY36')
handler=TimedRotatingFileHandler('py3612.log',when='s',interval=2,backupCount=100,encoding='utf-8')
logger.addHandler(handler)
for i in range(100):
    logger.warning('测试调试{}'.format(time.time()))
    time.sleep(0.1)