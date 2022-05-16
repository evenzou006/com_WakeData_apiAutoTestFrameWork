import os

# 项目路径
BASE_PATH = os.path.dirname(os.path.dirname(__file__)).replace('\\', '/')

# 配置文件路径
# 邮件配置文件路径
EMAIL_CONFIG_PATH = BASE_PATH + '/config/email_conf.yaml'

# 日志配置文件路径
LOG_CONFIG_FILE = BASE_PATH + '/config/logs_conf.yaml'

# mysql配置文件路径
MYSQL_CONFIG_FILE = BASE_PATH + '/config/mysql_conf.yaml'

# REDIS配置文件路径
REDIS_CONFIG_FILE = BASE_PATH + '/config/redis_conf.yaml'

# 测试报告配置文件路径
REPORT_CONFIG_PATH = BASE_PATH + '/config/report_conf.yaml'

# excel用例配置文件
EXCEL_CASE_PATH = BASE_PATH + '/testcase/excel_case/'

# 运行环境配置文件
RUN_ENV_PATH = BASE_PATH+'/config/environment_conf.yaml'

# pytest测试用例的yaml数据驱动文件路径
pytest_datadriver_path = BASE_PATH+'/testcase/testcase_pytest/data_driver/'

print(BASE_PATH)
