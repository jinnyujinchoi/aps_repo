N, V = map(int, input().split())
arr = list(map(int, input().split()))
idx = -1 # 찾는 값이 없으면 -1 반환
for i in range(N):
    if arr[i] == V:
        idx = i
        break
print(idx)
"""
6 4
2 7 5 3 1 7
-1
"""
