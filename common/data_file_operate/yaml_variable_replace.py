# @Author : EvenZou
# @CreateTime : 2022/5/10 10:05
# @FileName : yaml_variable_replace.py
import copy
import yaml
from string import Template
from common.data_file_operate.yaml_file_load import yaml_read_str
from common.file_path import pytest_datadriver_path


# def yaml_replace2(source_data: str, replace_data: dict):
#     """
#     替换yaml文件中的 $ 或者 ${} 变量
#     :param source_data: 原数据，即需要被替换的变量,变量需满足规则 ${} 或 $
#     :param replace_data: 替换后的数据
#     :return:
#     """
#     print(type(source_data), "res_data= ", source_data)
#     # 把safe_substitute()传入的字典，替换Template()中原数据相同键名的变量值，safe_substitute()在匹配过程中自动忽略匹配不到的字符串
#     variable_replace = Template(source_data).safe_substitute(**replace_data)
#     data_to_dict = yaml.safe_load(variable_replace)
#     print(type(data_to_dict), data_to_dict)
#     return data_to_dict


def object2null(s):
    """
    将空字符转为null_object字符
    :param s:传入一个字典
    :return:返回处理了字典中空值和None值的字典

    items()用法，dict.items()
    x = {'title':'python web site','url':'www.iplaypy.com'}
    x.items() 通过items()方法，把字典转换成如下格式
    [('url', 'www.iplaypy.com'), ('title', 'python web site')]

    """
    new = copy.deepcopy(s)
    for key, value in s.items():
        if "" == value:
            new[key] = "null_object"
        if value is None:
            new[key] = ""
    return new


def yaml_replace(source_data: str, replace_data: dict):
    """
    替换yaml文件中的 $ 或者 ${} 变量，并通过object2null()处理空值问题
    :param source_data: 原数据，即需要被替换的变量,变量需满足规则 ${} 或 $
    :param replace_data: 替换后的数据
    :return:
    """
    variable_replace = Template(source_data).safe_substitute(object2null(replace_data))
    data_to_dict = yaml.safe_load(variable_replace)
    data_to_str = str(data_to_dict)
    final_data = eval(data_to_str.replace("null_object", ""))
    # print(type(final_data), final_data)
    return final_data  # 再次转换为字典


if __name__ == "__main__":
    yaml_data = yaml_read_str(pytest_datadriver_path + 'check_login.yaml')
    print('yaml_data', yaml_data)
    variable_data = {"body": "{'id': '5463456'}", "Cookie": "67856645786789"}
    yaml_replace(yaml_data, variable_data)