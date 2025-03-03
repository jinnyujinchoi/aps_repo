# 배열 최소 합
def solve(arr, N):
    s = 0   # 합 초기화
    i = 0
    while i < N:    # 배열 끝에 다다를 때까지
        min_val = 10  # 각 행 최솟값 초기화
        for j in range(N):
            if min_val > arr[i][j]:
                min_val = arr[i][j]
        s += min_val
        i += 1
    return s

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {solve(arr, N)}")