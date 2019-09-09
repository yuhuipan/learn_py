class Person:
    def __init__(self, name='Charlie', age=8):
        self.name = name
        self.age = age

    # 类实例方法
    def say(self, content):
        print(content)


class Bird:

    # 类方法
    @classmethod
    def fly(cls):
        print('类方法fly:', cls)

    # 类静态方法
    @staticmethod
    def info(p):
        print('静态方法info:', p)
