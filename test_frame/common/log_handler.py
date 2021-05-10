import logging
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler
def my_logger(name='',
              logger_level='',
              hand_level='',
              matter='',
              file_name=None,
              file_level=''):
    logger=logging.getLogger(name)
    logger.setLevel(logger_level)
    handler=logging.StreamHandler()
    handler.setLevel(hand_level)
    logger.addHandler(handler)
    mat=logging.Formatter(matter)
    handler.setFormatter(mat)
    if file_name:
        file_handler=RotatingFileHandler(file_name,maxBytes=1024 * 1024 * 10,backupCount=10,encoding='utf-8')
        file_handler.setLevel(file_level)
        logger.addHandler(file_handler)
        file_handler.setFormatter(mat)
    return logger
if __name__=='__main__':

    loggs=my_logger(file_name='logs')

    loggs.info('正常运行')
    loggs.error('出错啦')
    loggs.debug('调试信息')

# 收集器

    import os
    from test_frame.config import path
    file_name_path=os.path.join(path.logs_path,'lesson36.log')
    logger=my_logger(file_name=file_name_path,
                     name='root',
                     logger_level='INFO',
                     hand_level='INFO',
                     matter='%(asctime)s-%(name)s-%(levelname)s-%(message)s-%(filename)s-%(lineno)s',
                     file_level='INFO')













