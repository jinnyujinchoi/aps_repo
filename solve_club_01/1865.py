def dfs(row, m):
    global N, ans
    if row == N:
        ans = max(ans, m)
        return

    if m <= ans:
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(row+1, m*work[row][j])
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]
    visited = [0]*N
    ans = 0     # 최댓값 초기화

    dfs(0, 1)
    print(f"#{tc} {ans*100:.6f}")