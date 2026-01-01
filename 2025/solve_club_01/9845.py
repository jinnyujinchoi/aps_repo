def f(n):
    if n > N:              # 존재하지 않는 경우 0 리턴
        return 0
    if tree[n] == 0:        # 리프 노드가 아닌 경우
        r1 = f(n*2)         # 왼쪽 자식노드의 값
        r2 = f(n*2+1)         # 오른쪽 자식노드의 값
        tree[n] = r1 + r2
    return tree[n]


T = int(input())
for tc in range(1, T+1):
    # N 노드의 개수 / M 리프 노드의 개수 / L 값 출력 노드 번호
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)

    for _ in range(M):
        node, val = map(int, input().split())
        tree[node] = val

    f(1)       # 자식 노드의 합 구하기
    print(f"#{tc} {tree[L]}")