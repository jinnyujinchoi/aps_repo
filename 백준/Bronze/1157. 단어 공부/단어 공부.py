from collections import Counter

word = input().upper()
cnt = Counter(word)

max_cnt = max(cnt.values())
ans = '?'

for k, v in cnt.items():
    if v == max_cnt:
        if ans == '?':
            ans = k
        else:
            ans = '?'
            break
print(ans)