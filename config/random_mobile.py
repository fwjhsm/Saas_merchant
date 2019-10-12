import random


def random_mobile():

    """
    随机生成手机号
    可能出现已注册手机号，
    问题不大
    """
    mobile_2 = random.randint(100000000,999999999)
    mobile = "13"+ str(mobile_2)
    return mobile


# print(random_mobile())