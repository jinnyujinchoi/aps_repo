dotx = []
doty = []
for _ in range(3):
    x, y = map(int, input().split())
    if x in dotx:
        dotx.remove(x)
    else:
        dotx.append(x)
    if y in doty:
        doty.remove(y)
    else:
        doty.append(y)

print(dotx[0], doty[0])