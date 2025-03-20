import sys
sys.stdin = open("sample_in.txt", "r")

import heapq

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    INF = int(21e8)     # 무한대
    ds = [[INF] * N for _ in range(N)]  # 누적거리 초기화
    ds[0][0] = 0

    # (누적 거리, x좌표, y좌표)
    pq = [(0, 0, 0)]

    while pq:
        current_cost, i, j = heapq.heappop(pq)

        # 이미 더 작은 경로면 pass
        if current_cost > ds[i][j]:
            continue

        # 목적지에 도달하면 탐색 종료
        if i == N - 1 and j == N - 1:
            break

        # 델타 배열 검사
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                # 기본 비용 추가 +1
                new_cost = current_cost + 1
                # 목표 지점 더 높은 경우 차이만큼 추가
                if cost[ni][nj] > cost[i][j]:
                    new_cost += (cost[ni][nj] - cost[i][j])
                # 더 적은 비용으로 이동 가능하면
                if ds[ni][nj] > new_cost:
                    ds[ni][nj] = new_cost
                    heapq.heappush(pq, (new_cost, ni, nj))

    result = ds[N-1][N-1]
    print(f"#{tc} {result}")