T = 10
for tc in range(1, T+1):    # 케이스 별로 처리
    N = int(input())    # 건물 개수
    arr = list(map(int, input().split()))

    total_build = 0  # 조망권 확보된 세대 수

    for i in range(2, N-2):
        compare_build = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]    # 비교 건물 리스트
        high_build = max(compare_build)     # 비교 건물 중 가장 높은 건물

        if arr[i] > high_build:
            view_build = arr[i] - high_build
            total_build += view_build

    print(f'#{tc} {total_build}')

