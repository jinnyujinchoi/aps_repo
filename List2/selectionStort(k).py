N, k = map(int, input().split())
arr = list(map(int, input().split()))

def select(arr, k):
    for i in range(0, k):
        min_index = i
        for j in range(i+1, N):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr[k-1]

print(select(arr, k))