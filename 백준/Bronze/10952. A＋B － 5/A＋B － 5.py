while 1:
    A, B = map(int, input().split())
    ans = A + B
    if A == 0 and B == 0:
        break
    print(ans)