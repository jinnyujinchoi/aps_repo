def dfs(stop):
    global ans
    if stop+bus[stop] >= N-1:   # 충전지 합이 N이 되면 종료
        return

    next_stop = 0
    max_i = 0
    for i in range(stop+1, stop+bus[stop]+1):
        if next_stop < i + bus[i]:
            next_stop = i + bus[i]
            max_i = i
    ans += 1
    dfs(max_i)

T = int(input())
for tc in range(1, T+1):
    N, *bus = map(int, input().split())
    ans = 0
    dfs(0)
    print(f"#{tc} {ans}")