#!/usr/bin/python3
# coding=utf-8
import logging
import time
from os import path
from config.globalparam import log_path

class Logger():
    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        rq = '{0}_UI_aotumation_test_report.log'.format(time.strftime("%Y_%m_%d"))
        log_name = path.join(log_path, rq)
        print(log_name)

        # 创建handler，写入日志到log文件
        fh = logging.FileHandler(log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 创建handler，写入日志控制台
        ch = logging.StreamHandler(log_name)
        ch.setLevel(logging.INFO)

        # 定义log的输出格式
        formatter = logging.Formatter('%(asctimes)-%(name)s-%(levelname)-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def getlog(self):
        return self.logger

