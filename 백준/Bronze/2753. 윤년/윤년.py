ans = 0 # 디폴트는 윤년이 아님
y = int(input())
# 400의 배수 이거나 (4의 배수이면서 100의 배수가 아닐 때)
if y%400 == 0 or (y%4 == 0 and y%100 != 0):
    ans = 1
print(ans)