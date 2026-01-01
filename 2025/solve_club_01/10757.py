def in_order(n):
    global cnt
    if n<=N:        # 완전이진트리
        in_order(n*2)
        tree[n] = cnt
        cnt += 1
        in_order(n*2+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())        # 정점 수

    tree = [0]*(N+1)
    cnt = 1
    in_order(1)
    print(f"#{tc} {tree[1]} {tree[N//2]}")