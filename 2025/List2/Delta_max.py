N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_v = 0 # 최대값 초기화
for i in range(N):
    for j in range(N):
        s = arr[i][j] # 합은 일단 본인 포함
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 상하좌우
            for c in range(1,K+1): # 확장범위 구간
                ni, nj = i+di*c, j+dj*c # di, dj에 K 곱하면 확장
                if 0<=ni<N and 0<=nj<N:
                    s += arr[ni][nj]
        if max_v < s:
            max_v = s
print(max_v)
