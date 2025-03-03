def is_gwalho(txt):
    top = -1
    s = ['']*len(txt)
    for i in range(len(txt)):
        if txt[i] == '(' or txt[i] == ')' or txt[i] == '{' or txt[i] == '}':
            top += 1
            s[top] = txt[i]
            if s[top-1] == '(' and s[top] == ')':
                top -= 2
            elif s[top-1] == '{' and s[top] == '}':
                top -= 2
    if top == -1:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    txt = input()
    print(f"#{tc} {is_gwalho(txt)}")