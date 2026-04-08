ans = ''
list_r = []
# 입력받기
for _ in range(3):
    r = int(input())
    list_r.append(r)

# 판별]
cnt = len(set(list_r))
if sum(list_r) != 180: # 삼각형이 아니면
    ans = 'Error'
else:
    if cnt == 1:
        ans = 'Equilateral'
    if cnt == 2:
        ans = 'Isosceles'
    if cnt == 3:
        ans = 'Scalene'

print(ans)
