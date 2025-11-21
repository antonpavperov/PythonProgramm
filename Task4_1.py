import random
import math

t = random.randint(1, 10 ** 4)

for n in range(t):
    n = random.randint(1, 9)
    a = []
    for i in range(n):
        a.append(random.randint(1, 9))
        if i == n-1:
            result = math.prod(a)
            print(result)
