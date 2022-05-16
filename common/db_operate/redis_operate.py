import redis
from common.data_file_operate.yaml_file_load import yaml_read_dict
from common.file_path import REDIS_CONFIG_FILE
from common.logs import log

redis_connect_txt = yaml_read_dict(REDIS_CONFIG_FILE)['redis_config']
print(redis_connect_txt)


class RedisOperate:
    """
        redis执行器
    """

    def __init__(self, db):
        self.redis = redis.Redis(host=redis_connect_txt['host'], port=redis_connect_txt['port'], db=db, password=redis_connect_txt['password'])

    def get(self, key):
        """
        通过key名获取redis的value值
        :param key:
        :return:
        """
        try:
            return str(self.redis.get(key), encoding="utf-8")
        except Exception as e:
            log.error(f"redis的{key}值获取失败，失败信息：{e}")

    def set(self, key, value, ex=None, px=None, nx=None, xx=None):
        """
        设置redis的key值,可设置过期时间
        :param key:
        :param value:
        :param ex:
        :param px:
        :param nx:
        :param xx:
        :return:
        """
        try:
            self.redis.set(key, value, ex, px, nx, xx)
        except Exception as e:
            log.error(f"redis的{key}值设置失败，失败信息：{e}")


if __name__ == '__main__':
    print(RedisOperate(0).get("name"))
    RedisOperate(1).set("name", "baba")
