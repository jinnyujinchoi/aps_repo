sub = list(map(int, input().split()))
n = len(sub)
for i in range(1<<n):
    s_sub = 0 # 초기화
    for j in range(n):
        if i&(1<<j):
            s_sub += sub[j]

    if s_sub == 0:
       for j in range(n):
           if i&(1<<j):
                print(sub[j], end=' ')
       print()