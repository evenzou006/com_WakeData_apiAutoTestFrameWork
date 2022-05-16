from random import random
import pytest


@pytest.fixture(scope='module', autouse=True)  #scope：fixture的执行级别（session、module、class、function）
def token_fix():
    print('fixture前置方法执行')
    token = int(str(random()).split('.')[1])
    print(f'token={token}')
    yield # yield关键字前面的表示前置方法，后面的表示后置方法
    print('fixture后置方法执行')