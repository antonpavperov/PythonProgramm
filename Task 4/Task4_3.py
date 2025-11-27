t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    num_str = input().strip()
    d_str = str(d)


    insert_pos = n
    for i in range(n):
        if num_str[i] < d_str:
            insert_pos = i
            break


    result = num_str[:insert_pos] + d_str + num_str[insert_pos:]
    print(result)


