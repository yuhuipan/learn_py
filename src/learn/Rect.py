class Rect:
    def __init__(self, area):
        self.__area = area

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        self.__area = value

    @area.deleter
    def area(self):
        self.__area = 0


rect = Rect(30)
