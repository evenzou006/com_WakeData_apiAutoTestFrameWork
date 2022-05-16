import pytest
import allure
import json
from common.logs import log
from common.api_keywords import ApiKey
from common.file_path import pytest_datadriver_path
from common.data_file_operate.yaml_file_load import yaml_read_dict
from common.data_file_operate.yaml_variable_replace import yaml_replace
from common.get_run_envm import run_host

host = run_host()  # 当前运行环境的地址


# noinspection PyGlobalUndefined
class TestUserManage:

    def test_get_token(self, token_fix):
        my_token = token_fix
        print('！！！！！my_token= ', my_token, '!!!host= ', host)

    @allure.story("用户管理")
    @pytest.mark.parametrize('data', (yaml_read_dict(pytest_datadriver_path+'TestUserManage.yaml'))['UserLogin'])
    def test_user_login(self, data):
        global Cookie   # 设置全局变量，实现接口依赖
        allure.dynamic.title(data['title'])
        # 拼接发送请求字典
        request_data = {
            'url': host + data['url'],
            'headers': data['headers'],
            'body': data['body']}
        res = getattr(ApiKey(), data['method'].lower())(**request_data)  # 发送接口请求
        if str(res.status_code)[0] in ('2', '3'):  # 判断状态码是否2或者3开头
            log.info(f'请求发送成功，用例名称：{data["title"]},请求方法：{data["method"]},请求参数：{request_data},'
                     f'状态码：{res.status_code},响应报文：{json.loads(res.text)}')
            # Cookie = requests.utils.dict_from_cookiejar(res.cookies)  # 获取dict格式的cookie
            Cookie = res.headers['Set-Cookie']  # 获取string格式的cookie
            # print(f'Cookie={Cookie}')
        else:
            log.error(f'请求发送失败，用例名称：{data["title"]},请求方法：{data["method"]},请求参数：{request_data},'
                      f'状态码：{res.status_code},响应报文：{res.text}')
        try:
            assert request_data['body']['password'] == 'Poly123~'
            assert res.status_code == 200
            assert request_data['body']['username'] == 15012312313
        except AssertionError:
            log.error(f'断言失败！预期：【username=15012312313，password=Poly123~】，实际：【username='
                      f'{request_data["body"]["username"]},password={request_data["body"]["password"]}】')
            raise AssertionError('断言失败')


    @allure.story("检查用户登陆情况")
    @pytest.mark.parametrize('data', yaml_read_dict(pytest_datadriver_path+'check_login.yaml'))
    def test_check_login(self, token_fix, data):
        source_data = data  # yaml文件中的原数据
        print('\\n')
        print('!!!!!!!source_data=', source_data)

        replace_data = {"Cookie": Cookie, "Authorization": token_fix}  # cookie是上个接口获取的参数，Authorization是fixture中返回的
        final_data = yaml_replace(str(source_data), replace_data)
        print('!!!!!!!final_data= ', final_data)
        allure.dynamic.title(final_data['title'])
        dict_data = {
            'url': host + final_data['url'],
            'headers': final_data['headers'],
            'timeout': 60
        }
        # dict_data['headers']['token'] = token_fix
        print('!!!!!!!dict_data= ', dict_data)
        res = getattr(ApiKey(), data['method'].lower())(**dict_data)
        response_body = res.text
        print(f'---------response_body= ', response_body)
        status = ApiKey().get_text(response_body, '$.status')[0]  # jsonpath提取的结果为list格式，所需需要通过下标取值
        print("!!!!!!!!!!!!!status= ", status)
        assert status == 200