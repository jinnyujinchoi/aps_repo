# 부분 배열 개수 구하기 함수
def ssafy_part(arr, N):
    cnt = 0     # 면적이 가장 큰 배열 수 초기화
    max_size = large_part()
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for ni, nj in [[i+k, j+k]]:
                    if 0<=ni<N and 0<=nj<N:
                        if arr[i][j] == arr[ni][nj]:
                            if (ni-i+1)*(nj-j+1) == large_part(arr, N):
                                cnt += 1
    return cnt
# 제일 큰 부분 배열 크기 구하기
def large_part(arr, N):
    space = 0   # 면적 초기화
    max_space = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):  # i <= ni / j <= nj 범위
                for ni, nj in [[i+k, j+k]]:
                    if 0<=ni<N and 0<=nj<N:
                        if arr[i][j] == arr[ni][nj]:
                            space = (ni-i+1)*(nj-j+1)
            if max_space < space:
                max_space = space
    return max_space

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {ssafy_part(arr, N)}")