def dfs(n):
    global ans
    if n == N:  # 끝까지 다 내려오면 가능
        ans += 1    # 횟수 추가
        return

    for j in range(N):
        # j는 열 / n+j 는 우상향 대각선 값(모두 일치함) / n-j는 좌하향 대각선 값(모두 일치함)
        if v1[j] == v2[n+j] == v3[n-j] == 0:    # 확인해야 할 배열 싹 다 비었으면
            v1[j] = v2[n+j] = v3[n-j] = 1   # 방문 표시
            dfs(n+1)    # 밑으로 내려가세요
            v1[j] = v2[n+j] = v3[n-j] = 0 # 해제제


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = 0
    v1 = [0]*N  # 열 확인 배열
    v2 = [0]*(2*N)  # 우상향 대각선 확인 배열
    v3 = [0]*(2*N)  # 좌하향 대각선 확인 배열

    dfs(0)
    print(f"#{tc} {ans}")