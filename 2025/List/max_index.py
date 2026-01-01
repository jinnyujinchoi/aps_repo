N = int(input())
arr = list(map(int, input().split()))
max_idx = 0 # 첫 원소가 최대 원소 가정
for i in range(1,N):
    if arr[max_idx] < arr[i]:
        max_idx = i
print(max_idx)
"""
6
2 7 5 3 1 4
1
"""