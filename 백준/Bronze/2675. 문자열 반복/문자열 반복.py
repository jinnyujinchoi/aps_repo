T = int(input())
for _ in range(T):
    R, S = input().split()
    r = int(R)
    for i in S:
        print(i*r, end='')
    print()