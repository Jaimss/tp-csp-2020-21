def sum(x, y):
    half = y/2
    return half*(y+x)


def sum_old(x, y):
    sum = 0
    for i in range(1, y+1):
        sum += i
    return sum

listnum = [(1, 200), (3, 500), (1,200000), (654363, 634575364164723)]

for n in listnum:
    print(f'{sum(n[0], n[1])} == {sum_old(n[0], n[1])}')
