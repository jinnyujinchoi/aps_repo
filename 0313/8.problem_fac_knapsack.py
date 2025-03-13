n = 3
target = 30
things = [(5, 50), (10, 60), (20, 140)]     # kg, Price

# kg 당 가격으로 어떻게 정렬?
# 정렬: price / kg
things.sort(key=lambda x: (x[1] / x[0]), reverse=True)

total = 0
for kg, price in things:
    pass
