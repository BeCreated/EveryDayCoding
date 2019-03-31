import time


# 计算函数的大概运行时间
def run_time(func):
    def inner_func(*args, **kwargs):
        start_time = time.time();
        func(*args, **kwargs);
        end_time = time.time();
        run_time = end_time - start_time;
        print(run_time)
        return None
    return inner_func


@run_time
def func_1():
    print('aaa')

if __name__ == '__main__':
    func_1()