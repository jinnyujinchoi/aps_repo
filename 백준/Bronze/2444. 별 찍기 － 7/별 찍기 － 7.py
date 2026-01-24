N = int(input())
for i in range(1, 2*N, 2):
    x = (2*N-1-i)//2
    print(' '*x + '*'*i)
for j in range(2*N-3, 0, -2):
    y = (2*N-1-j)//2
    print(' '*y + '*'*j)