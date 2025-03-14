T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0]*(N+1)     # 노드 값 저장해 줄 배열
    leaf = [list(map(int, input().split())) for _ in range(M)]  # 리프 노드 저장
    # 리프 값 트리에 넣어주기
    for i in range(M):
        arr[leaf[i][0]] = leaf[i][1]

    # arr 역순 탐색하여 완성
    for i in range(N, L-1, -1):     # L 까지만 채우도록 수정
        if arr[i]:      # 값이 있다면 넘어가기
            continue
        else:
            if (i*2+1 <= N) and arr[i*2+1]:     # 오른쪽 노드 값 있다면 넘어가기
                arr[i] = arr[i * 2] + arr[i * 2 + 1]
                # 넘어가기라는게 무슨 말임..? 있으면 둘 다 더한다, 없으면 왼쪽만 더한다 이거 아닌가
            else:
                arr[i] = arr[i * 2]

    print(f"#{tc} {arr[L]}")