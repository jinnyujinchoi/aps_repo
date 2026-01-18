# 동일 값 3개 -> 10000 + (a*1000)
# 동일 값 2개 -> 1000 + (a*100)
# -> 가장 큰 값*100
A, B, C = map(int, input().split())
ans = 0
if A == B == C:
    ans = 10000 + (A*1000)
elif A == B or A == C:
    ans = 1000 + (A*100)
elif B == C:
    ans = 1000 + (B*100)
else:
    ans = max(A, B, C)*100
print(ans)