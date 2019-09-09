class Student(object):
    count = 0

    def __init__(self, name):
        self.__name = name
        Student.count += 1

    def __get_name__(self):
        return self.__name


if Student.count != 0:
    print('测试失败')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败')
    else:
        lisa = Student('Lisa')
        if Student.count != 2:
            print('测试失败')
        else:
            print('Students:', Student.count)
            print('测试通过')
