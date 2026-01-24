A, B = map(str, input().split())
a, b = A[::-1], B[::-1]
ans = max(int(a), int(b))
print(ans)