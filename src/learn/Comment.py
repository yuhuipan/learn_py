class Comment:
    def __init__(self, detail, view_times):
        self.detail = detail
        self._view_times = view_times

    def info(self):
        print('一条简单的评论,内容是: %s' % (self.detail,))


c = Comment('疯狂Python讲义很不错', 20)
print(hasattr(c, 'detail'))
print(hasattr(c, '_view_times'))
print(hasattr(c, 'info'))
print(getattr(c, 'detail'))
print(getattr(c, '_view_times'))
print(getattr(c, 'info', 'default'))
print(getattr(c, 'age', 'default'))
setattr(c, 'detail', '毛泽东旧居')
setattr(c, '_view_times', '32')
print(c.detail)
print(c._view_times)
