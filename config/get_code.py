import random

from Saas_merchant.config.redis_link import redis_link


def get_code():
    # 获取验证码
    try:
        mobile = input("请输入手机号：")
        code = redis_link(mobile)

        print(code)

    except Exception as e:
        print("没有找到手机号 %s" % e)

get_code()

for i in range(random.randint(1,1000),1001):
    print(i)
    break