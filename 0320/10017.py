def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

T = int(input())
for tc in range(1, T+1):
    N, E = map(int,input().split()) # 마지막 번호
    V = N+1
    edges = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append((s, e, w))
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(V)]

    cnt = 0
    ans = 0
    for u, v, w in edges:
        if find_set(u) != find_set(v):
            union(u, v)
            cnt += 1
            ans += w

            if cnt == V-1:
                break
    print(f"#{tc} {ans}")