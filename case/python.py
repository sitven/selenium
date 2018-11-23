import logging

logger = logging.getLogger()  # logging对象
fh = logging.FileHandler("test.log")  # 文件对象
sh = logging.StreamHandler()  # 输出流对象
fm = logging.Formatter('%(asctime)s-%(filename)s[line%(lineno)d]-%(levelname)s-%(message)s')  # 格式化对象
fh.setFormatter(fm)  # 设置格式
sh.setFormatter(fm)  # 设置格式
logger.addHandler(fh)  # logger添加文件输出流
logger.addHandler(sh)  # logger添加标准输出流（std out）
logger.setLevel(logging.DEBUG)  # 设置从那个等级开始提示

logger.debug("debug Test")
logger.info("info Test")
logger.warning("warning Test")
logger.error("error Test")
logger.critical("critical Test")
