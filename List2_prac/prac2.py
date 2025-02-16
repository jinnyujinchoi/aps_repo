N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
total_sum = 0   # 절대값의 합 초기화
for i in range(N):
    for j in range(M):
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M:
                total_sum += abs(arr[ni][nj]-arr[i][j])
print(total_sum)