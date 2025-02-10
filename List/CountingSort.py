N = int(input())
arr = list(map(int, input().split()))

def countSort(arr, N):
    COUNTS = [0] * (max(arr)+1)  # max(DATA) + 1
    TEMP = [0] * N
    for i in range(N):      # 각 숫자의 개수(1단계)
        COUNTS[arr[i]] += 1

    for i in range(1, 5):       # COUNTS[i]까지의 합계
        COUNTS[i] += COUNTS[i-1]    # DATA[i]까지의 개수 1개 감소

    for i in range(N-1, -1, -1):    # 역순 탐색 (N-1 -> 0)
        COUNTS[arr[i]] -= 1
        TEMP[COUNTS[arr[i]]] = arr[i]

countSort(arr, N)
print(arr)
