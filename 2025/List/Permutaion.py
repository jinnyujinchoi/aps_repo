arr = list(map(int, input().split()))
for i1 in range(3):
    for i2 in range(3):
        if i1 != i2:
            for i3 in range(3):
                if arr[i3] != arr[i1] and arr[i3] != arr[i2]:
                    print(arr[i1], arr[i2], arr[i3])
