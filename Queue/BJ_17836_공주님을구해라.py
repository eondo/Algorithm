# 백준 17836. 공주님을 구해라!
# time :

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    global min_dist

    visited[x][y] = 0
    queue = []
    queue.append((x, y))
    total_dist = 10001

    while queue:
        px, py = queue.pop(0)

        if (px, py) == (n - 1, m - 1):
            if visited[px][py] < min_dist:
                min_dist = visited[px][py]
            return

        for d in range(4):
            nx = px + dx[d]
            ny = py + dy[d]

            if (
                0 <= nx < n
                and 0 <= ny < m
                and arr[nx][ny] != 1
                and visited[nx][ny] == -1
            ):
                visited[nx][ny] = visited[px][py] + 1
                queue.append((nx, ny))

                if (nx, ny) == sword:
                    sword_dist = visited[px][py] + 1
                    # print('sd', sword_dist)
                    total_dist = (
                        sword_dist + abs(n - 1 - sword[0]) + abs(m - 1 - sword[1])
                    )
                    # print(r, c)
                    # print(abs(n - 1 - r))
                    # print(abs(m - 1 - c))
                    # print('td', total_dist)

                    if total_dist <= t and total_dist < min_dist:
                        min_dist = total_dist

                if visited[nx][ny] > t:
                    if total_dist > t:
                        min_dist = 10001
                    else:
                        min_dist = total_dist
                    return


n, m, t = map(int, input().split())

arr = []

for r in range(n):
    row = list(map(int, input().split()))
    for c in range(m):
        if row[c] == 2:
            sword = (r, c)
    arr.append(row)

visited = [[-1] * m for _ in range(n)]
min_dist = 10001
bfs(0, 0)
# for line in range(n):
#     print(visited[line])
if min_dist == 10001:
    print('Fail')
else:
    print(min_dist)