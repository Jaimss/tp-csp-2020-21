x = lambda b, a: a * b

print(x(11, 12))


# other example
def my_fun(i):
    return lambda a: i * a


f = my_fun(2)
print(f(2))

some = lambda a: a * 3

print(some(1))

