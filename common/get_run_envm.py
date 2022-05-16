# -*- coding: utf-8 -*-
# @Author : EvenZou
# @CreateTime : 2022/5/16 18:26
# @FileName : get_run_envm.py
from common.data_file_operate.yaml_file_load import yaml_read_dict
from common.file_path import RUN_ENV_PATH


def run_host():
    yaml_data = yaml_read_dict(RUN_ENV_PATH)
    host = yaml_data['run_host']
    return host