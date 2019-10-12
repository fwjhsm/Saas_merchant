import os

def delete():
    for i in os.listdir(os.getcwd()):
        if i.endswith("html"):
            os.remove(i)
            print("删除文件: " + i + " 成功")
        else:
            print("没有可删除文件")


delete()