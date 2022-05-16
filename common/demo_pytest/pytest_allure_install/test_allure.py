import os
import allure
import pytest
from common.logs import log


def step_01():
    username = "jojo"
    # print(f'{username}=jojo')
    return username


def step_02():
    password = "123456"
    return password


class TestEditPage:

    @allure.step("执行登陆用例")
    def test_01(self):
        step_01()
        step_02()
        try:
            assert step_01() == 'joo'
        except AssertionError:
            log.error(f"断言失败！预期结果：【joo】与实际结果：【{step_01()}】不符")
            raise AssertionError("断言失败")

    @allure.step("查询商品用例")
    def test_02(self):
        print("查询商品")


if __name__ == '__main__':
    pytest.main(['test_allure.py', '--alluredir', './allure_result'])
    # os.system('allure generate ./common/demo_pytest/pytest_allure_install/allure_result/ -o ./report/ --clean')
