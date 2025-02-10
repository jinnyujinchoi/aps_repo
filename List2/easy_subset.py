arr = [3,6,7,1,5,4]
n= len(arr)

for i in range(1<<n):
    sub_lst = []
    for j in range(n):
        if i & (1<<j):
            sub_lst.append(arr[j])

    print(sub_lst)