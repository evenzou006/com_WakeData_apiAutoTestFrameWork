from common.data_file_operate.yaml_file_load import yaml_read_dict
from common.file_path import BASE_PATH, LOG_CONFIG_FILE
from loguru import logger
import time
import os


def logging():
    """
    把运行产生的日志，加入到指定的日志文件中
    :return:
    """
    logs_config = yaml_read_dict(LOG_CONFIG_FILE)['log_config']
    # print('logs配置文件' + LOG_CONFIG_PATH)

    # 全部日志：用来存放系统运行产生的全量日志
    logger.add(BASE_PATH + logs_config['logs_path'] + logs_config['all_logname'], format=logs_config['log_format'],
               filter="", level=logs_config['log_level'], rotation=logs_config['alllog_maxsize'],
               retention=logs_config['log_savetime'], encoding='utf-8')

    # 每天日志：存放系统在当天运行产生的日志，按天生成一个日志文件，在log_clean()把该日志设置成了只保存当天最后一次运行产生的日志
    logger.add(BASE_PATH + logs_config['logs_path'] + logs_config['date_logname'], format=logs_config['log_format'],
               filter="", level=logs_config['log_level'], rotation=logs_config['datelog_starttime'],
               retention=logs_config['log_savetime'], encoding='utf-8')

    # # 单次日志
    # logger.add(BASE_PATH + logs_config['logs_path'] + logs_config['single_logname'], format=logs_config['log_format'],
    #            filter="", level=logs_config['log_level'], rotation=logs_config['datelog_starttime'],
    #            retention=logs_config['log_savetime'], encoding='utf-8')

    # 错误日志文件：只存放系统运行中产生的错误级别的日志
    logger.add(BASE_PATH + logs_config['logs_path'] + logs_config['error_logname'],
               format=logs_config['log_format'],
               filter="", level='ERROR', rotation=logs_config['datelog_starttime'],
               retention=logs_config['log_savetime'], encoding='utf-8')

    return logger


def log_clean():
    """
    清除指定日志文件名的日志文件中的内容
    :return:
    """
    now_date = time.strftime("%Y-%m-%d", time.localtime(time.time()))  # 系统当前日期
    now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time()))  # 系统当前时间
    logfile_name = f'{BASE_PATH}/logs/log_{now_date}.log'  # 单次执行的日志文件名
    os.system(f'echo > {logfile_name}')  # 若日志文件中存在内容，则先清空，然后重新记录本次运行的日志
    log.info(f"======开始执行本次用例(当前时间：{now_time})======")
    # os.system(f'cat {logpathname}')  # 打开日志文件


log = logging()


# log.error("error级日志")
# log.info("info级日志")
# log.debug("debug级日志")
# log.warning("warn级日志")
