def DFS(i, G, N):  # i정점에 방문하는 함수, 목적지 G, 마지막정점번호 N
    global cnt
    if i == G:
        cnt += 1
    else:
        visited[i] = 1
        for j in adj_l[i]:  # 인접리스트
            # for j in range(N):  # 인접행렬
            #   if adj_m[i][j]: # 0또는 1로만 표시된 인접행렬인 경우
            if visited[j] == 0:
                DFS(j, G, N)
        visited[i] = 0  # 다른 경로를 통해 정점 i에 방문하는 경우 대비


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    arr = list(map(int, input().split()))
    S, G = map(int, input().split())  # 출발, 도착

    adj_l = [[] for _ in range(N + 1)]
    adj_m = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(E):
        n1, n2 = arr[i * 2], arr[i * 2 + 1]
        adj_l[n1].append(n2)  # 방향성그래프 인접리스트

        adj_m[n1][n2] = 1  # 방향성그래프 인접행렬

    cnt = 0
    visited = [0] * (N + 1)  # 진행방향으로 방문표시
    DFS(S, G, N)
    print(f'#{tc} {cnt}')