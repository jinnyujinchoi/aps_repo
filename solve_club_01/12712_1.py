T = int(input())
def fly_kill(lst): # 최대값 함수 정의
    fly_kill = 0 # 최대값 초기화
    for i in range(N):
        for j in range(N):
            s_kill = fly[i][j]
            for di, dj in lst:
                for c in range(1,M):
                    ni, nj = i+di*c, j+dj*c
                    if 0 <= ni < N and 0 <= nj < N:
                        s_kill += fly[ni][nj]
            if fly_kill < s_kill:
                fly_kill = s_kill
    return fly_kill
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    cross = [[0,1],[1,0],[0,-1],[-1,0]] # + 순회
    diagonal = [[1,1],[1,-1],[-1,-1],[-1,1]] # x 순회
    # +, X 값 비교
    c_kill = fly_kill(cross)
    x_kill = fly_kill(diagonal)
    if c_kill > x_kill:
        result = c_kill
    else:
        result = x_kill
    print(f"#{tc} {result}")