def in_order(n):        # 중위 순회
    if n <= N:          # 최대 정점 번호 이내인 경우 유효
        in_order(n*2)   # 왼쪽 자식
        print(tree[n], end='')      # 붙여서 출력
        in_order(n*2+1) # 오른쪽 자식

T = 10
for tc in range(1, T+1):
    N = int(input())        # 노드 개수
    tree = [0]*(N+1)
    for _ in range(N):
        v, c, *child = input().split()
        tree[int(v)] = c    # 완전이진트리 저장

    print(f"#{tc}", end=' ')
    in_order(1)
    print()                 # 다 찍고 행 바꿔 주기기