import random

headscount = 0
tailscount = 0

for _ in range(100000):
    i = random.randrange(1, 3)
    if i == 1:
        headscount+=1
    if i == 2:
        tailscount+=1

print(f'Heads: {headscount} | Tails: {tailscount}')
