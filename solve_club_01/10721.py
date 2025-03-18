# dfs 함수(n -> 0부터 행 시작, s -> 합)
def dfs(n, s):
    global ans  # 최솟값 저장 변수
    if ans <= s:  # 이미 커졌다면 가지치기
        return
    if n == N:  # 모든 행 탐색 완료하면
        ans = min(ans, s)   # 갱신 후 종료
        return              # 재귀 종료 이전 호출 돌아감

    for j in range(N):      # 현재 행에서 열 탐색
        if visited[j] == 0: # 방문한 적x
            visited[j] = 1  # 방문 처리
            dfs(n+1, s+arr[n][j])   # 다음 행 탐색
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = N*10      # 최댓값 설정
    visited = [0]*N # 방문 표시
    dfs(0,0)    # 0번째 행부터 탐색 시작

    print(f"#{tc} {ans}")