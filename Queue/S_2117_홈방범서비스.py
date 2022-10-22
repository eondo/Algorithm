# 2117. [모의 SW 역량테스트] 홈 방범 서비스
# time :
# idea
'''
1. 시작칸에서 마름모꼴 범위를 확인하고, 그때 카운트되는 1을 개수를 세야함
2. 마름모꼴 범위는 K에 따라 달라지는데, 그러면 달라지는 K에 대해서 위를 반복해야 하니까 K를 기준으로 반복문
3. 그 반복문은 비용 - M * 그 범위의 1값 개수 >= 0일 동안으로 while문?
4. 그렇게 while문마다 얻는 값을 서비스 받는 집 수로 치고, 이걸 max값으로 업데이트
5. 중심으로부터 마름모꼴로 퍼져나가니까 bfs 이용

문제
1. 그럼 한 칸에 접근해서 k를 증가시키면서 확인하고 싶은데,
사실 집 개수도 k를 정해야 몇 개가 포함될지 알 수 있는 것 아닌가?
- 생각했던 그림 : while K * K + (K - 1) * (K - 1) - cnt * m >= 0: 하고 밑에 k += 1 해가면서!


구현
1. 이차원 리스트에서 1인 값에서 출발하는 경우만 골라서 접근하자(위험)
2. 칸에 접근하면 거기서 k만큼 마름모꼴로 그 범위를 탐색하고 1을 카운트하자
    2-1) 이때 k는 1부터 어디까지 반복하냐면 수익 >= 0 일 때까지
3. 해당 칸에서 k마다 최대 집 개수를 카운트해서 max_cnt와 비교해서 업데이트하든 말든 하자
4. 위 작업을 이차원 리스트의 1인 칸마다 다 검사하고 마지막으로 나오는 max_cnt가 답


new
1. 모든 집을 다 포함시킨 게 최대 이득이니까 이걸로 k의 상한선을 알 수 있음!
    why? 모든 집을 다 포함시켜서 얻는 m * home_cnt가 k = ?일때의 비용보다 작은 경우가 존재하니까
2. 그러면 k의 최대값이 주어지니까 거기서 하나씩 줄여가면서 모든 칸을 다 접근해서 돌아보기
'''
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    global max_cnt

    for k in range(1, max_k + 1):
        visited = [[0] * n for _ in range(n)]
        visited[x][y] = 1
        home_cnt = 0
        queue = []
        queue.append((x, y))

        while queue:    # 근데 이제 k - 1만큼 움직일 수 있다는 걸 어디다 넣어줄지 고민해보자면...?
            px, py = queue.pop(0)

            if home[px][py] == 1:
                home_cnt += 1

            for t in range(4):
                nx = px + dx[t]
                ny = py + dy[t]

                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and visited[px][py] <= k - 1:
                    visited[nx][ny] = visited[px][py] + 1
                    queue.append((nx, ny))

        if m * home_cnt - (k * k + (k - 1) * (k - 1)) < 0:
            home_cnt = 0

        if home_cnt > max_cnt:
            # print(x, y, 'k:', k, 'cnt:', cnt)
            max_cnt = home_cnt


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())

    home = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if home[i][j] == 1:
                cnt += 1

    z = 1
    while cnt * m - (z * z + (z - 1) * (z - 1)) >= 0:
        z += 1  # while문 빠져나왔으면 더이상 안 되는 상태인 거니까 나온 k에 -1 해줌!

    # print(cnt)
    # print(z)

    max_k = z - 1   # k의 상한선
    max_cnt = 0
    # 모든 칸에 접근해보러 가자!
    for i in range(n):
        for j in range(n):
            bfs(i, j)

    print(f'#{tc} {max_cnt}')
