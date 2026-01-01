# 고대 구조물 찾기
def find_treasure(arr, N, M):
    max_r = 2  # 가로에서 가장 긴 보물 길이
    max_c = 2  # 세로에서 가장 긴 보물 길이
    # 가로 찾기
    for i in range(N):
        t_len = 0
        for j in range(M):
            if arr[i][j] == 1:
                t_len += 1
            else:
                break
                t_len = 0
        if max_r < t_len:
            max_r = t_len
    # 세로 찾기
    for j in range(M):
        t_len = 0
        for i in range(N):
            if arr[i][j] == 1:
                t_len += 1
            else:
                break
                t_len = 0
        if max_c < t_len:
            max_c = t_len
    if max_r < max_c:
        return max_c
    elif max_r > max_c:
        return max_r
    elif t_len == 1:
        return 0

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {find_treasure(land, N, M)}")