# 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트
# time : 25m
# idea
'''
처음과 끝이 모두 1(사무실)인 리스트 사이에서 목적지 구역 n까지 경로를 기록해야 한다.
그렇다면 2부터 n까지의 숫자가 어떻게 순서가 되어있든 다들 한 번씩 들르기만 하면 된다.
1. 그러니까 2부터 n까지 위 숫자로 된 순열을 만들자
2. 그 순열을 처음과 끝이 1인 리스트 사이에 붙여서 해당 값을 경로라고 하자
3. 구한 최종 경로 리스트를 for문으로 돌면서 i와 i+1을 인덱스로 하는 배터리값을 더하자
'''

def per(i): # 방문해야 할 n들로 순열을 만들고 최종 루트에 대한 배터리 사용량을 구하는 함수
    global minV

    if i == len(n_to_visit):            # 하나의 순열이 완성된 경우
        route = [1] + n_to_visit + [1]  # 1. 1이 처음과 끝으로 된 최종 경로 완성
        value = 0                       # 해당 경로의 배터리 사용량

        for j in range(len(route) - 1): # 2. n -> n 경로의 배터리 사용량을 for문으로 더함
            value += cost[route[j] - 1][route[j + 1] - 1]

        if value < minV:                # 3. 그 배터리 사용량과 현재 최소값 비교 및 갱신
            minV = value
        return
    else:                               #. 순열을 만드는 과정
        for k in range(i, len(n_to_visit)):
            n_to_visit[i], n_to_visit[k] = n_to_visit[k], n_to_visit[i]
            per(i + 1)
            n_to_visit[i], n_to_visit[k] = n_to_visit[k], n_to_visit[i]

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]  # 경로 사이의 배터리 사용량 정보
    minV = 100000                                               # 초기 최소값

    n_to_visit = [i for i in range(2, n + 1)]       # N을 가기 우해 들러야 할 구역들을 모은 리스트
    per(0)      # 0인덱스부터 순열 만들러 함수를 실행
    print(f'#{tc} {minV}')