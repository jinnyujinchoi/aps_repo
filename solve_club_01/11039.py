def max_area(arr, N):
    max_s = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:  # 넓이 구하기 시작
                w = h = 0    # 가로 세로 초기화
                # 가로 찾기
                for w in range(j, N):
                    if arr[i][w] == 1:
                        w += 1
                    else:
                        break
                # 세로 찾기
                for h in range(i, N):
                    for w in range(j, j+w):
                        if arr[h][j] == 1:
                            h += 1
                        else:
                            break
                s = w*h
                if max_s < s:
                    max_s = s
    return max_s

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {max_area(square, N)}")