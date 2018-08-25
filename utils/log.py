# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-7-24 12:20
# @File     : log.py

import os
import logging
from logging.handlers import TimedRotatingFileHandler
from utils.base_configuration import LOG_PATH


LEVEL = {'NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'}
"""日志等级：critical > error > warning > info > debug"""


class Log(object):
    def __init__(self, log_name="framework"):
        """实例化logger"""
        self.logger = logging.getLogger(log_name)
        logging.root.setLevel(logging.NOTSET)
        self.file_name = 'log'
        self.backup = 5
        self.console_level = 'NOTSET'
        self.file_level = 'DEBUG'
        self.format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    def print_log(self):
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.format)
            console_handler.setLevel(self.console_level)
            self.logger.addHandler(console_handler)
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup,
                                                    delay=True,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.format)
            file_handler.setLevel(self.file_level)
            self.logger.addHandler(file_handler)
        return self.logger


if __name__ == '__main__':
    Log('log').print_log().debug('test')
