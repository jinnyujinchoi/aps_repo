
def cal():
    if card[i] == '+':
        card[i+1] = card[i-1] + card[i+1]
    elif oper[i] == '-':
        card[i+1] = card[i-1] - card[i+1]
    elif oper[i] == '*':
        card[i+1] = card[i-1] - card[i+1]
    else:
        card[i+1] = card[i-1] // card[i+1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    oper = list(map(int, input().split()))
    card = [0]*(2*N-1)