N = int(input())
arr = list(map(int, input().split()))

def bubbleSort(arr, N):
    for i in range(N-1, 0, -1): # 범위의 끝 위치
        for j in range(i):      # 비교할 왼쪽 원소 인덱스
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubbleSort(arr, N)
print(arr)