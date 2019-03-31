# 可以传递参数的装饰器

def login():
    print('请输入用户名：')


def limit_route(route):
    if route == 'login':    
        def begin_func(func):
            def inner(*args, **kwargs):
                print('欢迎来访...')
                func(*args, **kwargs)
            return inner
        return begin_func
    else:
        def limit_func(func):
            def inner(*args, **kwargs):
                print('请重新登录!')
                login()
            return inner
        return limit_func


@limit_route('login')
def login_route(name):
    print('肖申克监狱欢迎{0}'.format(name))


if __name__ == '__main__':
    login_route('jack')
