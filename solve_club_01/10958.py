def qsort(arr, l, r):
    if l<r:
        s = hoare(arr, l, r)
        qsort(arr, l, s-1)
        qsort(arr, s+1, r)

def hoare(arr, l, r):
    p = arr[l]
    i = l
    j = r
    while i<=j:
        while i<=j and p >= arr[i]:
            i += 1
        while i<=j and p <= arr[j]:
            j -= 1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    qsort(arr, 0, N-1)
    print(f"#{tc} {arr[N//2]}")