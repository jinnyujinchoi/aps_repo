A, B = map(int, input().split())
t = A*60 + B - 45
if A == 0 and B < 45:
    h = 23
else:
    h = t//60
m = t%60
print(h, m)