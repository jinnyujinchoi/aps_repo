# V - A 까지만 도달하기
A, B, V = map(int, input().split())
h = A - B # 하루 증가량
needH = V - A # 올라 가야 할 높이
day = needH//h
if V <= A: # 첫 날 도착 가능하다면
    ans = 0
else:
    if needH%h == 0: # 나누어 떨어지면
        ans = day
    else:
        ans = day + 1
print(ans+1)