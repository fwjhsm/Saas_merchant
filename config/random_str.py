import random

list1 = ["哼","哈","二","将","6","小","灵","同","齐","天","大","圣","冯伟杰","in","0903",'2','B','A','ww']

# 生成随机索引
num = random.randint(0,len(list1)-1)


def random_str():
    str1 = list1[num] * 5 + list1[num-1]
    return str1

