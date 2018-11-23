# coding=utf-8
from config import globalparam
import logging
import time
import os

class Logger():
    """
    不理解
    调用格式为：
    mylogger = Logger(logger=类名)
    mylogger.debug( message="暂停一秒.")
    """
    def __init__(self, logger='root'):
        self.logger = logging.getLogger(logger)

    def __printconsole(self, level, message):
        # 定义log路径名称
        log_name = os.path.join(globalparam.log_path, time.strftime('%Y_%m_%d'+'_UI_automated_test.log'))


        # 创建一个logger(记录器),设置log级别
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义日志输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        if level == 'debug':
            self.logger.debug(message)          # logging.getLogger(logger).debug(message)
        elif level == 'info':
            self.logger.info(message)           # logging.getLogger(logger).info(message)
        elif level == 'warning':
            self.logger.warning(message)        # logging.getLogger(logger).warning(message)
        elif level == 'error':
            self.logger.error(message)          # logging.getLogger(logger).error(message)
        elif level == 'critical':
            self.logger.critical(message)       # logging.getLogger(logger).critical(message)

        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__printconsole('debug', message)

    def info(self, message):
        self.__printconsole('info', message)

    def warning(self, message):
        self.__printconsole('warning', message)

    def error(self, message):
        self.__printconsole('error', message)

    def critical(self, message):
        self.__printconsole('critical', message)


