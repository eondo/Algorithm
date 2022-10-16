# 1238. [S/W 문제해결 기본] 10일차 - Contact D4
# time :
# idea
'''
인접한 정점을 동시에 연락을 취하는 점 -> BFS의 특징!
이미 연락 받은 상대는 다시 연락하지 않는 것 -> visited 필요
인접 그래프로 해서 만들고 싶은데 1부터 100까지 칸을 만들기

1. 인접 그래프를 통한 BFS!
2. 전화 받는 순서를 visited[전 거] + 1 해서 채우기
3. visited값이 가장 큰 칸의 마지막 인덱스 뽑기
'''
def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = 1

    while queue:
        p = queue.pop(0)
        for next in graph[p]:               # 다음 인접 번호에 대해서
            if visited[next] == 0:          # 아직 접근하지 않은 번호라면
                queue.append(next)          # 큐에 저장 후
                visited[next] = visited[p] + 1  # 접촉한 순서를 그 전 사람의 +1로 저장


for tc in range(1, 2):
    n, start = map(int, input().split())
    graph = [[] for _ in range(101)]        # 인접 그래프 만들기 위함
    graph2 = dict()
    visited = [0] * (101)

    info = list(map(int, input().split()))

    for i in range(n // 2):
        graph[info[i * 2]].append(info[i * 2 + 1])

    bfs(start)

    last_num = 0
    last_idx = -1

    for idx, value in enumerate(visited):
        if value >= last_num:
            last_num = value
            last_idx = idx

    print(f'#{tc} {last_idx}')