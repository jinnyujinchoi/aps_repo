T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0 # 최대값 초기화
    # +모양 순회
    for i in range(N):
        for j in range(N):
            cross_kill = fly[i][j]
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                for c in range(1,M):
                    ni, nj = i+di*c, j+dj*c
                    if 0 <= ni < N and 0 <= nj < N:
                        cross_kill += fly[ni][nj]
            if max_kill < cross_kill:
                max_kill = cross_kill
    # x자 순회
    for i in range(N):
        for j in range(N):
            x_kill = fly[i][j]
            for di, dj in [[1,1],[1,-1],[-1,-1],[-1,1]]:
                for c in range(1,M):
                    ni, nj = i+di*c, j+dj*c
                    if 0 <= ni < N and 0 <= nj < N:
                        x_kill += fly[ni][nj]
            if max_kill < x_kill:
                max_kill = x_kill
    print(f"#{tc} {max_kill}")