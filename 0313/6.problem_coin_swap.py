coin_lst = [500, 100, 50, 10]   # 큰 동전부터 앞으로 작성함
target = 1730
cnt = 0

for coin in coin_lst:
    charge = target // coin
    cnt += charge
    target -= coin*charge
print(cnt)