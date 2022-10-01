import sys
input = sys.stdin.readline

from heapq import heappush, heappop


def dij(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, min_node = heappop(heap)

        if min_dist > distance[min_node]:
            continue

        for next in graph[min_node]:
            next_node = next[0]
            dist = next[1]

            new_dist = min_dist + dist

            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


node_cnt, edge_cnt = map(int, input().split())
graph = [[] for _ in range(node_cnt + 1)]
for _ in range(edge_cnt):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
v1, v2 = map(int, input().split())
INF = 99999999
distance = [INF] * (node_cnt + 1)

go_here = [1, v1, v2, node_cnt]
answer = 0
for i in range(len(go_here) - 1):
    dij(go_here[i])
    answer += distance[go_here[i + 1]]
print(answer)