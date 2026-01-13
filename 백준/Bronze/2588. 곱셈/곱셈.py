A, B = (int(input()) for _ in range(2))
b1 = B//100
b2 = (B - b1*100)//10
b3 = (B - (b1*100 + b2*10))
ans = [
    A*b3,
    A*b2,
    A*b1,
    A*B
]
print(*ans, sep="\n")