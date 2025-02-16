def is_concave(arr, N):
    # 행 순회 검증
    for i in range(N):
        o_len = 0
        for j in range(N):
            if arr[i][j] == 'o':
                o_len += 1
            if o_len == N:
                return 'YES'
            else:
                return 'NO'
    for j in range(N):
        o_len = 0
        for i in range(N):
            if arr[i][j] == 'o'
                o_len += 1
            if o_len == N:
                return 'YES'
            else:
                return 'NO'

    # 대각선 순회
    for di, dj in [[1,1],[-1,-1]]:
        ni = i + di
        nj = j + dj
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj] == '.':
                return 'NO'
    else:
        'YES'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print(f"#{tc} {is_concave(arr, N)}")