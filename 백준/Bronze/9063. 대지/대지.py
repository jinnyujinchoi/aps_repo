N = int(input())
dot_x = set()
dot_y = set()
ans = 0
for _ in range(N):
    x, y = map(int, input().split())
    # x, y 집합을 만들고, max - min
    dot_x.add(x)
    dot_y.add(y)
# 리스트 길이가 1이면 0
if len(dot_x) == 1 or len(dot_y) == 1:
    ans = 0
else:
    a = max(dot_x) - min(dot_x)
    b = max(dot_y) - min(dot_y)
    ans = a*b
print(ans)