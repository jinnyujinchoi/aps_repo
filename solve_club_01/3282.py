T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())            # N은 물건 개수 / K는 최대 부피
    lst = [[0, 0]]                              # 빈 2차원 배열
    for _ in range(N):
        lst.append(list(map(int, input().split())))     # 부피-가치 순으로 넣어주기

    # 물건을 넣었을 때 무게 별 최대 가치 표
    dp = [[0]*(K+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, K+1):
            w = lst[i][0]       # 부피는 리스트의 첫번째[0] 값
            v = lst[i][1]       # 가치는 리스트의 두번째[1] 값
            if j < w:           # 가방에 넣을 수 없다면
                dp[i][j] = dp[i-1][j]   # 위의 값 그대로
            else:               # 가방에 넣을 수 있다면
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

    print(f"#{tc} {dp[N][K]}")