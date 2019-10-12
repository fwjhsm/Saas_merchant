import redis
import re

from Saas_merchant.config.random_mobile import random_mobile


def redis_link(mobile):

    """从redis中取出验证码"""

    localhost = "192.168.199.240" #账号
    pwd = "123456" #密码
    r = redis.StrictRedis(host=localhost,port=6379,
                          password=pwd,
                          decode_responses=True,db=0)
    # mobile1 = str(mobile)
    # 拼接 key
    key = "register_verfify_code" + mobile
    key1 = "order_verfify_code" + mobile
    key2 = "register_key_"+mobile
    # print(key,"key")
    # print(type(key),"key 类型")
    # 根据 key 获取 value
    value = r.get(key)
    value1 = r.get(key1)
    value2 = r.get(key2)

    if value:
        value = re.search(r"(\d+)", value)
        return value.group(0),"注册登录验证码"
    elif value1:
        value1 = re.search(r"(\d+)", value1)
        return value1.group(0),"订单验证码"
    elif value2:
        return value2,type(value2)
        # value2 = re.search(r"(\d+)", value2)
        # return value1.group(0), "添加员工验证码"


# print(redis_link(15644789987))
# print(redis_link(15678899663))