# 1232. 사칙연산

def find_answer(v):
    if v:
        left = find_answer(ch1[v])
        right = find_answer(ch2[v])

        if tree[v] == '+':
            tree[v] = left + right
        elif tree[v] == '-':
            tree[v] = left - right
        elif tree[v] == '*':
            tree[v] = left * right
        elif tree[v] == '/':
            tree[v] = left / right
        else:
            pass
        return tree[v]  # !증요 - 꼭 있어야 하는 부분
    # else: # 기존 코드에는 이를 붙여주었으나 없어도 됨
    #     return 0

for tc in range(1, 2):
    n = int(input())
    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)
    tree = [0] * (n + 1)

    for _ in range(n):
        info = input().split()
        if len(info) == 2:
            tree[int(info[0])] = int(info[1])
        else:
            tree[int(info[0])] = info[1]
            ch1[int(info[0])] = int(info[2])
            ch2[int(info[0])] = int(info[3])

    find_answer(1)
    print(tree[1])