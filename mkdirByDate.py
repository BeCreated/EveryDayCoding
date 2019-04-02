import sys
import time
import os


def getTodayDate():
    today = time.localtime(time.time())
    format_day = time.strftime('%Y_%m_%d', today)
    return format_day

def checkDirAndCreate(dirname):
    if not os.path.exists(dirname):
        os.system('mkdir {}'.format(dirname))
    return True


# 根据日期创建文件夹
def mkdirByDate():
    param = sys.argv[1] if len(sys.argv)>1 else ''
    today = getTodayDate()
    dirname = "{0}_{1}".format(today, param)
    if checkDirAndCreate(dirname):
        print('文件夹：{}创建成功...'.format(dirname))

if __name__ == '__main__':
    mkdirByDate()
