N = int(input())
arr = list(map(int, input().split()))

def selectionSort(arr, N):
    for i in range(N-1):
        min_idx = i     # 첫 원소를 최소로 가정
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:     # 최소 원소 위치 갱신
                min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selectionSort(arr, N))