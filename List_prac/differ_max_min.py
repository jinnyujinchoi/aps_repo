T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    max_v = a[0]    # 첫 인덱스 값을 최댓값 지정
    min_v = a[0]    # 첫 인덱스 값 최솟값 지정
    for i in range(1, N):
        if max_v < a[i]:
            max_v = a[i]
        if min_v > a[i]:
            min_v = a[i]
    print(f"#{tc} {max_v - min_v}")