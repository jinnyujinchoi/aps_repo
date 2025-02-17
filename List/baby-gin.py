num = int(input())
c = [0]*12

for i in range(6):
    c[num%10] += 1  # 10 나눈 나머지 인덱스 추가
    num //= 10  # 몫만 남겨 주기~

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:   # tri 판별
        c[i] -= 3   # 배열에서 3개 삭제
        tri += 1    # tri 카운트 추가
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:   # run 판별
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1     # 배열에서 삭제해주기
        run += 1    # run 카운트 추가
        continue
    i += 1

print("Baby Gin" if tri+run == 2 else "Lose")