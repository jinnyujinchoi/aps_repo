import sys
sys.stdin = open("input (31).txt", "r")

# N*N visited 배열 만든다
# 해당 숫자에서 갈 수 있다면 1 기록
# 연속된 1의 길이가 가장 긴 곳이 정답!
# 같은 길이가 있다면, 작은 수가 정답 위치
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*(N*N+1)       # 숫자는 1부터 시작

    # 현재 위치 숫자 기준 상하좌우 확인 -> 1큰 곳이 있다면
    # visited 기록
    for i in range(N):
        for j in range(N):
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni, nj = i+di, j+dj
                # 범위 밖에 나가면 안됩니다이
                if 0<=ni<N and 0<=nj<N:
                    if arr[ni][nj] == arr[i][j] + 1:
                        visited[arr[i][j]] = 1  # 현재 숫자 다음 이동 가능
                        break                   # 나머지 방향 볼 필요x

    # 연속된 1의 개수 가장 긴 곳 찾기
    # 가장 긴 곳, 현재 몇 개, 출발지 찾기
    max_cnt = cnt = start = 0
    for  i in range(1, N*N+1):
        if visited[i] == 1:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                start = i - cnt
            cnt = 0             # 개수 초기화

    print(f"#{tc} {start} {max_cnt+1}")


