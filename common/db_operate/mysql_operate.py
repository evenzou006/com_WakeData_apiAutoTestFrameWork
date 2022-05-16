import pymysql
from common.data_file_operate.yaml_file_load import yaml_read_dict
from common.file_path import MYSQL_CONFIG_FILE
from common.logs import log
from tools.hash import my_aes_decrypt


class MysqlOperate:
    """
    mysql执行器
    """

    def __init__(self, dbname):
        """
        :param dbname: 需要操作的数据库库名
        """
        try:
            mysql_connect_txt = yaml_read_dict(MYSQL_CONFIG_FILE)['mysql_config']
            mysql_connect_txt['db'] = dbname  # mysql连接中，指定要操作的数据库名称
            # 对mysql连接配置中的密码进行aes解密
            mysql_connect_txt['password'] = my_aes_decrypt(mysql_connect_txt['password'], 'abcdefghjklmnopu', 'abcdefghjklmnopq')
            self.con = pymysql.connect(**mysql_connect_txt)  # 创建数据库连接
            log.info(f'数据库连接成功，连接信息:host={mysql_connect_txt["host"]}:{mysql_connect_txt["port"]}, '
                     f'user={mysql_connect_txt["user"]}, db={mysql_connect_txt["db"]}')
        except Exception as e:
            log.error(f"数据库连接失败，失败详情：{e}")
        else:
            self.cursor = self.con.cursor()  # 创建游标

    def db_close(self):
        """
        关闭游标和数据库连接
        """
        try:
            self.cursor.close()
            self.con.close()
            log.info("mysql数据库已关闭连接")
        except Exception as e:
            log.error(f"数据库关闭失败，失败原因：{e}")

    def query_sql(self, sql_script):
        """
        mysql查询sql语句
        :param sql_script:DQL脚本
        :return:执行查询语句后的查询结果
        """
        try:
            self.cursor.execute(sql_script)
            result_all = self.cursor.fetchall()
            log.info(f'msql脚本执行成功，执行sql= {sql_script}')
            # for result_one in result_all:
            #     print(result_one)
            print(result_all)
            return result_all
        except Exception as e:
            log.error(f"sql执行失败，失败信息:{e}")

    def execute_sql(self, sql_script):
        """
        sql执行（DDL，DML）
        :param sql_script: DDL/DML脚本
        """
        try:
            self.cursor.execute(sql_script)
            log.info(f'msql脚本执行成功，执行sql={sql_script}')
        except Exception as e:
            log.error(f"sql执行失败，失败信息:{e}")

    def count_sql(self, sql_script):
        """
        获取mysql查询到的数量
        :param sql_script: DQL脚本
        :return: 返回结果集的数量
        """
        try:
            res = self.cursor.execute(sql_script)
            log.info(f'msql脚本执行成功，执行sql={sql_script}')
            print(f'本次查询的结果条数 = {res}')
            return res
        except Exception as e:
            log.error(f"sql执行失败，失败信息:{e}")


if __name__ == '__main__':
    db = MysqlOperate('rs_user_sales')
    db.count_sql('select * from ztc_activity_rule')
    db.db_close()
    # MysqlOperate().execute_sql('delete * student')
