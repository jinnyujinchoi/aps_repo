N = int(input())
s = list(map(int, input()))
total = 0
for j in range(9-N):  # N은 길이
    cnt = 0
    for k in range(N//2):
        if s[j+k] != s[j+N-1-k]:
            break
        cnt +=1
    if cnt == N//2:  # 회문인 경우
        total += 1