import sys
sys.stdin = open("input (1).txt", "r")
# 이건 그냥 다익스트라 알고리즘
def dijkstra(s_node, arr):
    pq = [(0, s_node)]  # (누적거리, 노드번호)
    ds = [INF] * (N+1)      # (각 정점까지 최단)누적거리 리스트 생성
    ds[s_node] = 0      # 시작노드 최단거리는 0

    while pq:
        d, node = heapq.heappop(pq)

        # 이미 더 작은 경로로 온 적이 있다면 pass
        if ds[node] < d:
            continue

        for next_info in arr[node]:
            next_d = next_info[0]       # 다음 노드 가기 위한 가중치
            next_node = next_info[1]    # 다음 노드 번호

            # 다음 노드로 가기 위한 누적 거리
            new_d = d + next_d
            # 이미 같은 가중치거나, 더 작은 가중치로 온 적이 있다면
            if ds[next_node] <= new_d:
                continue
            # next_node 까지 도착하는데 비용은 new_d
            ds[next_node] = new_d
            heapq.heappush(pq, (new_d, next_node))

    # 맨 앞 값은 빼고 출력해야 함
    return ds[1:]

import heapq
INF = int(21e8)     # 21억 (무한대 의미)

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())     # 노드 / 간선 / 생파
    s_node = 0  # 문제에 따라 다를 수o
    to_party = [[] for _ in range(N+1)]      # 파티에 가요
    from_party = [[] for _ in range(N+1)]    # 돌아와요

    for _ in range(M):
        u, v, w = map(int, input().split())
        from_party[u].append((w, v))     # 역방향 u -> v
        to_party[v].append((w, u))      # 정방향 v -> u

    to_party_ds = dijkstra(X, to_party)         # i -> X
    from_party_ds = dijkstra(X, from_party)     # X -> i
    result = [x+y for x, y in zip(to_party_ds, from_party_ds)]

    ans = max(result)
    print(f"#{tc} {ans}")