n = int(input())
a = list(map(int, input().split()))

total_sum = sum(a)


if total_sum != 0:
    print("YES")
    print(1)
    print(1, n)
else:
    found = False
    for i in range(1, n):
        left_sum = sum(a[:i])
        right_sum = sum(a[i:])

        if left_sum != 0 and right_sum != 0:
            print("YES")
            print(2)
            print(1, i)
            print(i + 1, n)
            found = True
            break

    if not found:
        print("NO")
