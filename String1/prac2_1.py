N = int(input())
txt = input()
total = 0
for j in range(8-N+1):
    for k in range(N//2):
        if txt[j+k] != txt[j+N-1-k]:
            break
    else:
        total += 1
print(total)