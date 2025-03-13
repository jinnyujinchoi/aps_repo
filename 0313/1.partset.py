arr = ['o', 'x']
path = []
name = ['MIN', 'CO', 'TIM']


def print_name():
    print('{', end='')
    for i in range(3):
        if path[i] == 'o':
            print(name[i], end='')
    print('}')


def recur(cnt):
    if recur == 3:
        print_name()
        return

    # 가지의 개수
    # recur(포함하는 경우)
    # recur(하지 않는 경우)
    for i in range(2):
        path.append(arr[i])
        recur(cnt + 1)
        path.pop()


recur(0)