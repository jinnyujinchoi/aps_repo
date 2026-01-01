for _ in range(1, 11):
    tc = int(input())
    road = [list(map(int, input().split())) for _ in range(100)]
    # X좌표 찾기
    goal_j = -1
    for j in range(100):
        if road[99][j] == 2:
            goal_j = j
            break
    # 스타트 지점으로 돌아가기
    i = 99      # X 좌표
    j = goal_j
    di = [0,0,-1]    # 좌 우 상 (우선순위 순)
    dj = [-1,1,0]
    dir = 0
    while i > 0:    # 0이 되면 종료
            ni, nj = i+di[dir], j+dj[dir]
            # 우선 순위 방향 탐색, 값이 1이면
            if 0<=ni<100 and 0<=nj<100 and road[ni][nj] == 1:
                road[i][j] = 0    # 지나간 자리 0 할당
                i, j = ni, nj   # i, j에 이후 좌표 할당
                continue
            dir = (dir+1)%3   # 방향 전환

    print(f"#{tc} {j}")