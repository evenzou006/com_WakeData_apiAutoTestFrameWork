import yaml

from common.file_path import pytest_datadriver_path


def yaml_read_dict(yaml_file):
    """
    加载yaml文件内容，并返回dict格式
    :param yaml_file: yaml文件
    :return: yaml_dict
    """
    with open(yaml_file, mode='r', encoding='utf-8') as fd:
        return yaml.load(fd, Loader=yaml.FullLoader)


def yaml_read_str(yaml_file):
    """
    加载yaml文件内容，并返回string格式
    :param yaml_file:
    :return: yaml_str yaml_dict
    """
    with open(yaml_file, encoding='utf-8') as fd:
        data = fd.read()
    return data


if __name__ == '__main__':
    yaml_data = yaml_read_str(pytest_datadriver_path + 'check_login.yaml')
    print('!!!!!!!!!yaml_data_str= ', yaml_data)
    yaml_data = yaml_read_dict(pytest_datadriver_path + 'check_login.yaml')
    print('!!!!!!!!!yaml_data_dict= ', yaml_data)