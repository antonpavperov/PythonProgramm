import math

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if 0 in a:
        a[a.index(0)] = 1  # увеличиваем один ноль до 1
    else:
        min_idx = a.index(min(a))
        a[min_idx] += 1  # увеличиваем минимальную цифру

    print(math.prod(a))