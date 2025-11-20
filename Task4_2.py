import random

a = random.randint(1,100)
print(a)
if 1 <= a <= 100:
    if a % 2 == 0:
        print("YES")
    else:
        print("NO")

