score = int(input())
ans = ''
if score < 60:
    ans = 'F'
elif score < 70:
    ans = 'D'
elif score < 80:
    ans = 'C'
elif score < 90:
    ans = 'B'
else:
    ans = 'A'
print(ans)