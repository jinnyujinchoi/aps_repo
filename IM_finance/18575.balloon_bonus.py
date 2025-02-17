def balloon_bonus(arr, N):
    max_val = 0     # 최댓값 초기화
    min_val = arr[0][0]
    # 최솟값 지정하기
    for di, dj in [[0,1],[1,0]]:
        for c in range(1, N):
            ni, nj = 0+di*c, 0+dj*c
            if 0 <= ni < N and 0 <= nj < N:
                min_val += arr[ni][nj]
    # 합 구하기
    for i in range(N):
        for j in range(N):
            bomb = arr[i][j]
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                for c in range(1, N):
                    ni, nj = i + di * c, j + dj * c
                    if 0<=ni<N and 0<=nj<N:
                        bomb += arr[ni][nj]
                        # 최댓값 / 최솟값 비교하기
            if max_val < bomb:
                max_val = bomb
            if min_val > bomb:
                min_val = bomb
    return max_val-min_val

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {balloon_bonus(board, N)}")