class Item:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __del__(self):
        print('删除方法执行')

    def info(self):
        pass


im = Item('鼠标', 29.8)
# del im
print(im.__dict__)
print(im.__dict__['_name'])
print(im.__repr__())
print('================')
print(im.__dir__())
print('================')
print(dir(im))
