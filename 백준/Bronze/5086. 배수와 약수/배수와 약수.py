while 1:
    a, b = map(int, input().split())
    ans = ''
    if a == 0 and b == 0:
        break
    # 첫 번째 수가 두 번째 수의 약수
    elif a < b and b % a == 0:
        ans = 'factor'
    elif a > b and a % b == 0:
        ans = 'multiple'
    # 첫 번째 수가 두 번째 수의 배수
    # 관계 없음
    else:
        ans = 'neither'
    print(ans)