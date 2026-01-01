N = int(input())
arr = list(map(int, input().split()))
s = 0 # 합 초기화
for i in range(N):
    s += arr[i]
print(s)
"""
6
2 7 5 3 1 4
22
"""