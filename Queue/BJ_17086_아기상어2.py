# 백준 17086. 아기 상어2
# time :
# idea
'''
상어가 있는 모든 곳들을 출발점으로 해서 다 돌아봐야 할 것 or 한 번만 visited 채우기 -> 전자!
- 가장 가까운 타 아기상어와 만나면 상어 한 마리가 출발점인 케이스는 종료 (안전거리 정의에 의해)
- 그럼 bfs로 돌다가 조건(1이면서 범위 내)만족하면 그 값을 안전거리 최대로 저장하고 break 종료
- 그 다음 상어 위치 봄
'''
dx = [0, 1, 0, -1, -1, 1, 1, -1]    # 우, 하, 좌, 상, 오위, 오아, 왼아, 왼위
dy = [1, 0, -1, 0, 1, 1, -1, -1]


def bfs():
    max_dist = 0

    while queue:
        px, py = queue.pop(0)
        # print(px, py)

        # if (px, py) != (x, y) and arr[px][py] == 1:
        #     print(x, y, '일 때 여기서 걸렸다!', px, py)
        #     safe_dist = visited[px][py] - 2
        #     break

        for d in range(8):
            nx = px + dx[d]
            ny = py + dy[d]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] != 1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[px][py] + 1

                if visited[nx][ny] > max_dist:
                    max_dist = visited[nx][ny]

    # for i in range(n):
    #     print(visited[i])
    # print(max_dist)
    return max_dist

    # if safe_dist > max_dist:
    #     max_dist = safe_dist
    #     print(x, y, '일 때 max는?', max_dist)
    #     return


n, m = map(int, input().split())
arr = []
queue = []
visited = [[0] * m for _ in range(n)]

for r in range(n):
    row = list(map(int, input().split()))
    for c in range(m):
        if row[c] == 1:
            queue.append((r, c))
            visited[r][c] = 1
    arr.append(row)

# print(n, m)
# print(queue)
# print(arr)
# print(visited)

answer = bfs()

print(answer - 1)