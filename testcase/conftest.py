import pytest


@pytest.fixture(scope='function')  # scope：fixture的执行级别（session、module、class、function）
def token_fix():
    print('fixture前置方法执行,获取token')
    token = '87967688987'
    return token


@pytest.fixture(scope='class', autouse=True)
def mysql_fix():
    print('fixture前置方法执行：测试数据初始化')
    yield
    print('fixture后置方法执行')

