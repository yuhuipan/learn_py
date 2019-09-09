def fun_a(fn):
    print('A')
    fn()
    return 'f_kit'


@fun_a
def fun_b():
    print('B')


# print(fun_b)


def foo(fn):
    def bar(*args):
        print('===1===', args)
        n = args[0]
        print('===2===', n * (n - 1))
        print(fn.__name__)
        fn(n * (n - 1))
        print('*' * 15)

    return bar


@foo
def my_test(a):
    print('==my_test函数==', a)


# my_test(10)
# my_test(6, 5)

def auth(fn):
    def auth_fn(*args):
        print('----模拟执行权限检查----')
        fn(*args)

    return auth_fn


@auth
def test(a, b):
    print('执行test函数，参数a: %s, 参数b: %s' % (a, b))


test(20, 50)


class User:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __hide(self):
        print('示范隐藏的hide方法')

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名长度必须在3~8之间')
        self.__name = name

    name = property(get_name, set_name)

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 18 or age > 70:
            raise ValueError('用户年龄必须在18~70之间')
        self.__age = age

    age = property(get_age, set_age)
