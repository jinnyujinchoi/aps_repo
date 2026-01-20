N, X = map(int, input().split())
arr = list(map(int, input().split()))
ans = [i for i in arr if i < X]
# ans = []
# for i in arr:
#     if i < X:
#         ans.append(i)
print(*ans)