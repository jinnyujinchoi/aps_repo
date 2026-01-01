T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 괴물의 수
    monster = [list(map(int, input())) for _ in range(10)]
    safe = 0    # 안전구역 초기화
    for i in range(10):
        for j in range(10):
            if monster[i][j] == 0:  # 0이면 통과
                continue
            if monster[i][j] == 1:  # R 괴물이면
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    for c in range(2):
                        ni, nj = i+di*c, j+dj*c
                        if 0 <= ni < 10 and 0 <= nj < 10:
                            monster[ni][nj] = monster[i][j]
                            continue
            if monster[i][j] == 2:  # G 괴물이면
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    for c in range(3):
                        ni, nj = i+di*c, j+dj*c
                        if 0 <= ni < 10 and 0 <= nj < 10:
                            monster[ni][nj] = monster[i][j]
                            continue
            if monster[i][j] == 3:  # B 괴물이면
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    for c in range(4):
                        ni, nj = i+di*c, j+dj*c
                        if 0 <= ni < 10 and 0 <= nj < 10:
                            monster[ni][nj] = monster[i][j]
                            continue
            if monster[i][j] == 4:  # 벽이면 통과
                continue

    for i in range(10):
        for j in range(10):
            if monster[i][j] == 0:  # 배열의 숫자가 0이면, 안전구역
                safe += 1

    print(f"#{tc} {safe}")