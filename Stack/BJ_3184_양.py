dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y):
    global sheep
    global wolf

    if arr[x][y] == 'o':
        sheep += 1
    elif arr[x][y] == 'v':
        wolf += 1

    visited[x][y] = True
    # print(visited)

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        # print(i, j, nx, ny)

        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != '#' and not visited[nx][ny]:
            dfs(nx, ny)


r, c = map(int, input().split())

arr = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

cnt_all_sheep = 0
cnt_all_wolf = 0

for i in range(r):
    for j in range(c):
        if visited[i][j] == False:
            if arr[i][j] != '#':
                sheep = 0
                wolf = 0

                dfs(i, j)

                if sheep > wolf:
                    cnt_all_sheep += sheep
                elif sheep <= wolf:
                    cnt_all_wolf += wolf

print(cnt_all_sheep, cnt_all_wolf)