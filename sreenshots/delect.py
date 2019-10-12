import os

def delete():
    for i in os.listdir(os.getcwd()):
        if i.endswith("png"):
            os.remove(i)
        else:
            print("没有可删除文件")


delete()