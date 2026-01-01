def solve(arr1, arr2):
    i = 0
    cnt = 0
    while i < N:
        if arr1[i] != arr2[i]:
            for j in range(i, N):
                if arr1[j] == 1:
                    arr1[j] = 0
                else:
                    arr1[j] = 1
            cnt += 1
        i += 1

    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print(f"#{tc} {solve(start, end)}")