import string


class A:
    pass


class B(A):
    pass


class C(A):
    pass


print([e for e in dir(string) if not e.startswith('_')])
print(A.__bases__)
print(B.__bases__)
print(C.__bases__)
print(A.__subclasses__())
print(B.__subclasses__())
print(C.__subclasses__())
print(string.__all__)
print(string.__file__)
