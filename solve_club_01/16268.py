T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0 # 최대값 초기화
    for i in range(N):
        for j in range(M):
            self = arr[i][j]
            sum_val = self # 합 초기화
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<M:
                    sum_val += arr[ni][nj]
            # 최대값 찾기
            if max_val < sum_val:
                max_val = sum_val
    print(f"#{tc} {max_val}")
