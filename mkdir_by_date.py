import sys
import time
import os


# 根据日期创建文件夹
def mkdir_by_date():
    # base_dir = os.path.abspath(__file__)
    param = sys.argv[1] if len(sys.argv)>1 else ''
    localtime = time.localtime(time.time())
    flocal = time.strftime('%Y_%m_%d', localtime)
    dir_name = "{0}_{1}".format(flocal, param)
    if not os.path.exists(dir_name):
        os.system('mkdir {}'.format(dir_name))
    else:
        print('{}文件夹已经存在...'.format(dir_name))

if __name__ == '__main__':
    mkdir_by_date()
