# 1953. 탈주범 검거

# tunnel 종류에 따라 갈 수 있는 방향
t_dx = {1: [-1, 0, 1, 0],
        2: [-1, 100, 1, 100],
        3: [100, 0, 100, 0],
        4: [-1, 100, 100, 0],
        5: [100, 100, 1, 0],
        6: [100, 0, 1, 100],
        7: [-1, 0, 100, 100]}

t_dy = {1: [0, -1, 0, 1],
        2: [0, 100, 0, 100],
        3: [100, -1, 100, 1],
        4: [0, 100, 100, 1],
        5: [100, 100, 0, 1],
        6: [100, -1, 0, 100],
        7: [0, -1, 100, 100]}

def bfs(x, y):
    queue = []
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        px, py = queue.pop(0)
        tunnel = arr[px][py]

        for k in range(4):
            if t_dx[tunnel][k] != 100 and t_dy[tunnel][k] != 100:   # 현재 k 방향으로 갈 수 있다면
                nx = px + t_dx[tunnel][k]
                ny = py + t_dy[tunnel][k]   # 일단 갈 수 있는 이동값으로 nx,ny를 구하고

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]: # 범위 안이고, 아직 안 간 곳이라면 1차 통과
                    n_tunnel = arr[nx][ny]
                    if n_tunnel > 0 and t_dx[n_tunnel][(k + 2) % 4] != 100 and t_dy[n_tunnel][(k + 2) % 4] != 100: # 그리고 방향 짝도 맞으면
                        queue.append((nx, ny))
                        visited[nx][ny] = visited[px][py] + 1


t = int(input())
for tc in range(1, t + 1):
    n, m, si, sj, time = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    bfs(si, sj)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if 0 < visited[i][j] <= time:
                cnt += 1

    print(f'#{tc} {cnt}')