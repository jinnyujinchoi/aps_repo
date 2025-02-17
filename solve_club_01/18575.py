def crazy_arcade(arr, N):
    max_val = 0
    min_val = arr[0][0]     # 첫번째 합을 최솟값으로 설정
    for di, dj in [[0, 1], [1, 0]]:
        for c in range(1, N):
            ni, nj = 0 + di * c, 0 + dj * c
            if 0 <= ni < N and 0 <= nj < N:
                min_val += arr[ni][nj]
    for i in range(N):      # 최댓값 구하기
        for j in range(N):
            water_bomb = arr[i][j]
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                for c in range(1, N):
                    ni, nj = i+di*c, j+dj*c
                    if 0<=ni<N and 0<=nj<N:
                        water_bomb += arr[ni][nj]
            if max_val < water_bomb:
                max_val = water_bomb
            if min_val > water_bomb:
                min_val = water_bomb
    return max_val-min_val

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {crazy_arcade(arr, N)}")
