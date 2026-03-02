N = int(input())
i = 2 # 2부터 나누기 시작
while i <= N:
    if N % i == 0:
        print(i)
        N //= i
    else:
        i += 1