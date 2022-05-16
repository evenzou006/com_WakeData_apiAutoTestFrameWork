import pytest

"""
pytest用例规范： https://docs.pytest.org
    1、pytest将在当前目录级其子目录中运行所有格式为test_*.py或者*_test.py的文件
    2、测试方法/函数默认必须是test开头
    3、测试类必须是Test开头

 Python测试用例发现约定
    *如果未指定任何参数,则收集从testpaths (如果已配置)或当前目录开始。另外,命令行参数可以在目录,文件名或节点ID的任何组合中使用。
    *递归到目录,除非它们匹配norecursedirs.
    *在这些目录中,搜索test_*.py或*_test.py.
    *从这些文件中,收集测试项目:
        *在类之外拥有test前级的测试函数或方法
        *在拥有Test前级中的测试类(不含_init_方法)中的拥有test前级的测试函数或方法
    可自定义测试发现规则
    pytest也可以发现使用标准的unittest.TestCase子类技术的测试用例(完全兼容unittest的原因)
    
pytest.main常用运行参数
    -s:用于关闭捕捉,从而输出打印信息
    -v:用于显示具体的信息
    -k:用例方法或者函数中存在指定关键字的运行
    -q：简化输出信息
    -x：出现失败用例，停止执行后面的用例
    指定用例执行：路径/xxx.py::用例方法名
    在第N个用例失败后，结束并退出测试执行：--maxfail=N
    查看执行时间最长的N个用例： --durations=N -vv
    禁用插件：-p no:插件名  如：-p no:doctest
    
标记表达式执行
    1、需引入pytest.ini文件，文件中定义标签名称
    2、在需要标记的用例名称上一行输入：@pytest.mark.[标签名]
    3、执行标签用例
        a、执行标记了指定标签的用例 pytest.main(['-m', '标签名'])
        b、执行不含指定标签的用例 pytest.main(['-m', 'not slow'])
    
多进程运行用例
    1、安装插件pytest-xdist   pip install pytest-xdist
    2、运行模式 
        pytest.main(['-n', '2', 'test_pytest_base.py'])   # 两个进程执行测试用例
        pytest.main(['-n', auto, 'test_pytest_base.py'])   # 使用与CPU同等核数的进程执行测试用例

失败用例重跑机制
     1、安装插件：pytest-rerunfailures
     2、失败重新执行：
        a、失败后立即重跑：pytest.main(['--reruns', '3', 'test_pytest_base.py'])  # 失败用例重跑3次
        b、失败后等待一定的时间再重跑：pytest.main(['--reruns', '3','--reruns-delay', '2', 'test_pytest_base.py']) # 失败重跑3次，每次执行时等待2s

pytest跳过用例执行方法
    1、有条件跳过测试函数，根据特定的条件，跳过符合条件的用例函数
        skipif(condition , reason=None)  # condition:跳过的条件  reason：标注跳过的原因
        使用语法：@pytest.mark.skipif(condition,reason='XXX')
        使用实例：@pytest.mark.skipif(condition=2>1, reason='废弃用例跳过')
    2、无条件跳过测试用例函数
        @pytest.mark.skip（reason='无条件跳过'）

前后置方法
    1、模块级别：setup_module()  teardown_module()
    2、类级别：setup_class()  teardown_class()  该方法的前一行需标记成：@classmethod
    3、方法级别：setup_method()  teardown_method(); 方法或函数级别 setup()  teardown()

pytest配置文件
    1、 pytest.ini
        a、定义标签
            markers =
                smoke
                slow
                happy
                serial
        b、命令行参数集
            addopts = -v --html=../../report/html_report.html --maxfail=2 --reruns=3 -n=2
                -v
        c、指定要运行的测试目录
            testpaths = ./  
        d、指定要运行的测试文件规则
            python_files = test_*.py
        e、指定要运行的用例类名规则
            python_classes = Test_A* Test_B*  # 可以同时加多个规则
        f、指定要运行的测试用例名称规则
            python_functions = test_*
    2、configtest.py   
        pytest特有的本地测试配置文件，既可以用来设置项目级别的fixture，也可以用来导入外部插件，还可以用来指定钩子函数，作用于她所在目录和子目录
        
pytest参数化
    1、单个多个参数
        parametrize(argnames, argvalues, indirect=False, ids=None, scope=None)
        常用参数：argnames：参数名   argvalues：参数值，类型为list 当参数为N个时，该用例将执行N次
        使用方法：@pytest.mark.parametrize(argnames,argvalues)
        
 
 pytest常用插件
    1、pytest-html 测试报告生成
    2、  
    
测试报告生成
    1、生成xml格式的测试报告
        pytest.main(['--junit-xml=../../report/xml_report.xml'])  在指定路径下生成xml格式的测试报告
    2、生成html格式的测试报告
        a、安装插件 pytest-HTML
        b、pytest.main(['--html=../../html_report.html'])  # 在指定路径下生成html格式的测试报告
    3、生成allure测试报告
        a、下载安装allure，配置allure环境变量
        b、安装allure-pytest库
        c、测试用例执行时，添加参数：alluredir，后面为测试结果json文件路径，如：pytest.main(['test_allure.py', '--alluredir', './allure_result'])
        d、用例执行完毕后，执行命令：'allure generate <测试结果json路径> -o <测试报告路径> --clean')
        
    
"""




@pytest.mark.smoke
def test_01():
    print("\n测试用例01，标签smoke")
    assert 1 != 2


@pytest.mark.happy
def test_02():
    try:
        print("\n测试用例02，标签happy")
        assert 1 != 1
    except AssertionError:
        raise AssertionError("断言失败")


@pytest.mark.slow
def test_03():
    print('\n测试用例03，标签slow')
    assert 6 < 7


@pytest.mark.happy
def test_04():
    try:
        print("\n测试用例04，标签happy")
        assert '3' not in '123'
    except AssertionError:
        raise AssertionError("断言失败")


@pytest.mark.smoke
@pytest.mark.parametrize('a', [10, 20])  # 参数化
def test_05(a):
    try:
        print(f'a={a}')
        re = a-15
        assert re > 0
    except AssertionError:
        raise AssertionError("断言失败")


@pytest.mark.parametrize('user,password', [('张三', 'qaz123'), ('李四', 'wsx123'), ('王五', 'edc123')])  # 参数化用这三组数据各跑一遍
def test_06(user, password):
    print(f'user= {user}，password={password}')


@pytest.mark.smoke
def test_07():
    print("\n测试用例07，标签smoke")


if __name__ == '__main__':
    # pytest.main(['-s', '-v'])  # -v：显示每个测试函数的执行结果；-s 用于显示测试函数中的print()函数输出
    pytest.main(['-q'])  # -q：只显示用例执行结果
    # pytest.main(['-s', '-k', '04'])  # 只执行测试用例名称含有字符'04'的测试用例
    # pytest.main(['--html=./report/html_report.html'])  # 生成html格式的测试报告
    # pytest.main(['--junit-xml=./report/xml_report.xml'])  # 生成xml格式测试报告
    # pytest.main(['--maxfail=2'])   # 用例执行中达到2条失败后，退出执行
    # pytest.main(['-m', 'slow'])   # 只执行被标记为指定标签(如slow)的测试用例
    # pytest.main(['-m', 'not slow'])  # 执行非指定标签(slow标签外的全部用例)外的全部用例
    # pytest.main(['-n', '2', 'test_pytest_base.py']) # 两个进程一起执行用例
    # pytest.main(['--reruns', '2', 'test_pytest_base.py'])  # 失败重跑2次
    # pytest.main(['--reruns', '3', '--reruns-delay', '2', 'test_pytest_base.py'])  # 失败重跑3次，每次执行时等待2s
    # pytest.main()
