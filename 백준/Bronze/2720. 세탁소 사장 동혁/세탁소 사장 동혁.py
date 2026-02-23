# 25-q, 10-d, 5-n, 1-p
T = int(input())
for _ in range(T):
    C = int(input())
    q = C // 25
    d = (C - q*25) // 10
    n = (C - (q*25 + d*10)) // 5
    p = (C - (q*25 + d*10 + n*5))
    print(q, d, n, p)