def fun(a: int) -> int:
    return a + 10


x: int = fun(3)
print(x.__add__(3))
