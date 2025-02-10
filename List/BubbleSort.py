N = int(input())
arr = list(map(int, input().split()))

def bubbleSort(arr, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubbleSort(arr, N)
print(arr)