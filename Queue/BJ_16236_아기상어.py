# 백준 16236. 아기상어
# time :
# idea
'''
상하좌우로 인접 한 칸식 이동
처음 아기 상어 크기 2
자기보다 작거나 같은 값만 지나갈 수 있음 / 자기보다 작은 것만 먹을 수 있음

더 이상 먹을 거 없음 -> 끝
거리가 가장 가까운 물고기를 찾아 거기로 이동
거리 동일하면 위, 왼쪽 기준으로 우선 선택

상어 크기 : 자기 크기만큼 먹으면 + 1 증가

먹을 물고기 찾아다니기 : bfs
- 한 번 bfs로 먹을 물고기 위치 확정하면? 한 번 bfs 끝나면?
1. 걸리는 시간 더해주기
2. 상어 거기로 옮김
3. 상어 크기 키울지 말지 판단
4. 그리고 나서 현재 위치에서 다시 bfs 실행

- bfs 실행 중에 모든 칸 다 돌때까지 먹을 수 있는 물고기 없으면? 중단,
그때까지 걸린 시간 출력

- 필요한 변수
1. 상어 크기
2. 지금까지 걸린 시간
3. visited
4. 현재 같은 거리의 물고기 위치 저장소
'''
dx = [0, 1, 0, -1]  # 우하좌상
dy = [1, 0, -1, 0]  # 우하좌상


def bfs(x, y, size):
    global is_done

    visited = [[0] * n for _ in range(n)]
    queue = []
    can_eat = []
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        px, py = queue.pop(0)

        for d in range(4):
            nx = px + dx[d]
            ny = py + dy[d]

            if 0 <= nx < n and 0 <= ny < n: # 일단 범위 안이고,

                if (arr[nx][ny] == 0 or arr[nx][ny] == size) and not visited[nx][ny]:
                    if not can_eat:
                        queue.append((nx, ny))
                        visited[nx][ny] = visited[px][py] + 1

                elif 0 < arr[nx][ny] < size and not visited[nx][ny]:
                    if not can_eat:
                        visited[nx][ny] = visited[px][py] + 1
                        can_eat.append((nx, ny, visited[nx][ny]))

                        dist = visited[nx][ny]  # 이 거리의 물고기만 이제 취급해!

                    elif visited[px][py] + 1 <= dist:   # 앞에서 지정한 최소 거리에 만족하는 애만 통과!
                        visited[nx][ny] = visited[px][py] + 1
                        can_eat.append((nx, ny, visited[nx][ny]))


    # print('먹으러가자', can_eat)
    # for i in range(n):
    #     print(visited[i])

    # 그럼 이제 먹으러 갈 후보지들 생겼다! 이중에 우선순위에 따라 그곳으로 가보자!
    if not can_eat: # 먹을 후보지 아예 없으면 중단 (엄마한테 간다고 함)
        is_done = True
        return
    else:
        return can_eat


n = int(input())

arr = []

for r in range(n):
    row = list(map(int, input().split()))
    for c in range(n):
        if row[c] == 9:
            si, sj = r, c
    arr.append(row)

# print(arr)
# print(shark)

# visited = [[0] * n for _ in range(n)]   # 매번 bfs 실행될 때마다 초기화
shark_size = 2
total_cnt = 0
eat_cnt = 0
is_done = False

while is_done == False:
    foods = bfs(si, sj, shark_size)
    # print('후보지', foods)

    if foods == None:
        break

    min_i = n
    min_j = n
    for pos in range(len(foods)):
        if foods[pos][0] < min_i:
            min_i = foods[pos][0]
            here = foods[pos]
        elif foods[pos][0] == min_i:
            if foods[pos][1] < here[1]:
                here = foods[pos]

    print('널 먹으러 가겠다', here)

    si, sj, time = here
    total_cnt += time - 1# 물고기 먹으러 가려면 시간 걸리니까 그거 더해줘야지
    arr[si][sj] = 0     # 물고기 먹고
    eat_cnt += 1

    if eat_cnt == shark_size:   # 진화할 조건에 만족하니? 그럼 커지게 하고
        shark_size += 1
        eat_cnt = 0

    # 이제 거길 출발지로 다시 bfs 돌러가야지!
for t in range(n):
    print(arr[t])
print(total_cnt)