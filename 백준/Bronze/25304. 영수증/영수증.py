X = int(input()) # 총 금액
N = int(input()) # 물건 종류 수
for _ in range(N):
    a, b = map(int, input().split())
    X -= a*b
if X == 0:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
