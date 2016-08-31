# -*- coding: utf-8 -*-
# Log class wraps python logging module to log spolight service
import logging
from logging import getLogger, handlers, Formatter


class Log:
    __log_level_map = {
        'debug' : logging.DEBUG,
        'info' : logging.INFO,
        'warn' : logging.WARN,
        'error' : logging.ERROR,
        'critical' : logging.CRITICAL
    }

    __my_logger=None

    @staticmethod
    def init(logger_name='spolight', log_level='debug', log_filepath='spolight/resource/log/spolight.log'):
        Log.__my_logger = getLogger(logger_name);
        Log.__my_logger.setLevel(Log.__log_level_map.get(log_level, 'warn'))

        formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        Log.__my_logger.addHandler(console_handler)

        file_handler = handlers.TimedRotatingFileHandler(log_filepath, when='D', interval=1)
        file_handler.setFormatter(formatter)
        Log.__my_logger.addHandler(file_handler)

    @staticmethod
    def debug(msg):
        Log.__my_logger.debug(msg)

    @staticmethod
    def info(msg):
        Log.__my_logger.info(msg)

    @staticmethod
    def warn(msg):
        Log.__my_logger.warn(msg)

    @staticmethod
    def error(msg):
        Log.__my_logger.error(msg)

    @staticmethod
    def critical(msg):
        Log.__my_logger.critical(msg)



