N = int(input())
arr = list(map(int, input().split()))
ans = 0
for x in arr:
    if x == 1:
        continue
    # 2부터 x까지 나머지가 0이어야 함
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        ans += 1
print(ans)