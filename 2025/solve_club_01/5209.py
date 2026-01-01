def dfs(row, current_s):
    global N, ans
    # 모든 행을 처리한 경우
    if row == N:
        ans = min(ans, current_s)   # 최솟값 갱신
        return
    # 누적 합이 최솟값보다 크거나 같으면
    if current_s >= ans:
        return

    for j in range(N):
        # 열이 선택되지 않았다면
        if not visited[j]:
            visited[j] = True   # 방문 표시
            dfs(row+1, current_s + cost[row][j])    # 다음 행 이동 + 비용 누적
            visited[j] = False  # 방문 해제제


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    ans = N**2*99       # 최댓값으로 초기화
    visited = [0]*N

    dfs(0, 0)
    print(f"#{tc} {ans}")
