if __name__ == '__main__':
    s = input('Gimme sum G: ')
    s = [char for char in s]
    d = {}
    for x in s:
        try:
            d[x] = d[x] + 1
        except:
            d[x] = 1

    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
    print(d)
    d = {k: v for k, v in sorted(d.items())}
    print(d)

    for (j, i) in enumerate(d):
        print('{} {}'.format(i, d[i]))
        if j == 2:
            break
