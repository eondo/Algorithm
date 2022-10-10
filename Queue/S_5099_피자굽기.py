# 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기 D3
'''
1. 화덕 크기가 피자 개수보다 작아서 한 번에 다 못 넣을 수도 있는데 어떡하지
2. 한바퀴 회전 하면 치즈가 줄어드는데 한 바퀴 회전했다는 걸 어떻게 표현하면 좋을까
3. 치즈 0되면 화덕에서 꺼내고 그 자리에 다음 순서 넣는다는 걸 어떻게 구현할까
4. 어떤 자료구조를 써야 다된 피자는 빠지고 그 자리에 다른 게 들어가고 표현? 큐
5. 큐를 써서, 맨 앞을 지나면 걔를 떼가지고 마지막에다가 치즈 반 녹은 상태 피자를 다시 넣어주는 방법?
'''

def bfs(num):
    queue = [num]
    for i in range(1, size):
        queue.append(i)

    while queue:
        #print(queue)
        p = queue.pop(0)
        cheeze = pizza[p] // 2

        if cheeze == 0:
            #print('i', i)
            #print('size', size)
            if i + 1 < pizza_cnt:
                i += 1
                #print('새로운 피자 들어가는 타임!', i)
                queue.append(i)
        else:
            pizza[p] = pizza[p] // 2
            queue.append(p)
        #print(pizza)

    return p

t = int(input())
for tc in range(1, t + 1):
    size, pizza_cnt = map(int, input().split())
    pizza = list(map(int, input().split()))

    answer = bfs(0)
    print(f'#{tc} {answer + 1}')
