# 사각지대는 몇 개?
def invisible_area(arr, N):
    full_cnt = where_s(area, N)        # 전체 감시 구역
    v_cnt = 0           # 감시 구역 수
    i, j = secu(area, N)    # 경비원 위치
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        for c in range(1, N):
            ni, nj = i+di*c, j+dj*c
            if 0<=ni<N and 0<=nj<N: # 구역을 벗어나지 않는 범위 내에
                if arr[ni][nj] == 1:   # 벽을 만나면
                    break               # 중지
                if arr[ni][nj] == 0:    # 0이면 계속
                    v_cnt += 1
    return full_cnt - v_cnt

# 빈 공간 개수 찾기
def where_s(arr, N):
    s_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                s_cnt += 1
    return s_cnt

# 경비원 찾기
def secu(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

T = int(input())
for tc in range(1, T+1):
    N = int(input())        # 구역 N*N
    area = [list(map(int, input().split())) for _ in range(N)]  # 구역 받기
    print(f"#{tc} {invisible_area(area, N)}")
