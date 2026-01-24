word = input().upper()
cnt = {}
for i in word:
   cnt[i] = cnt.get(i, 0) + 1
vals = list(cnt.values())
maxVal = max(vals)
if vals.count(maxVal) >=2:
    ans = '?'
else:
    ans = max(cnt, key=cnt.get)
print(ans)