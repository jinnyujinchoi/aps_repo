# 안전구역 찾기 함수
def safety_area(arr, N):
    s_cnt, mon_i, mon_j = where_mon(space, N)
    l_cnt = 0   # 레이저 침범 구역
    # 레이저 구역 개수 찾기
    for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
        for c in range(1, N):
            ni, nj = mon_i+di*c, mon_j+dj*c
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] == 1:    # 벽이면 탈출
                    break
                if arr[ni][nj] == 0:    # 안전구역이면 레이저
                    l_cnt += 1
    return s_cnt - l_cnt

# 안전 구역 & 괴물 위치 찾기
def where_mon(arr, N):
    mon_i = mon_j = 0
    s_cnt = 0 # 안전 구역
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                s_cnt += 1
            if arr[i][j] == 2:
                mon_i, mon_j = i, j
    return s_cnt, mon_i, mon_j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    space = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {safety_area(space, N)}")
