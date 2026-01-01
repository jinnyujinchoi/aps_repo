# 오목 판정 함수
def concave(arr, N):
    # o인 곳 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                # 4방향 탐색
                for di, dj in [[0,1],[1,0],[1,1],[1,-1]]:
                    cnt = 1 # 본인 포함
                    # 자신 기준 5개 연속 확인
                    for k in range(1, 5):
                        ni, nj = i+di*k, j+dj*k
                        # 구역 내 범위에서 'o'가 있으면
                        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 'o':
                            cnt += 1
                        else:   # 없으면 중단
                            break
                    if cnt == 5:
                        return "YES"
    return "NO"

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 배열 크기 받기
    stone = [list(input()) for _ in range(N)]
    print(f"#{tc} {concave(stone, N)}")