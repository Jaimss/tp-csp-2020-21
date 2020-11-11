class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_two_nums(self):
        return self.y + self.x


print(MyClass(3, 4).x)
d = MyClass(7, 10).add_two_nums()
print(d)
