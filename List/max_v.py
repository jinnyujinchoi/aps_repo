N = int(input())
arr = list(map(int, input().split()))
max_v = arr[0]
for i in range(1, N):
    if max_v < arr[i]:
        max_v = arr[i]
print(max_v)
"""
6
2 7 5 3 1 4
7
"""