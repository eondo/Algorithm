# s1) 프림 + 힙을 이용한 풀이
from heapq import heappush, heappop

import sys
input = sys.stdin.readline

def prim(start):
    visited = [False] * (village_cnt + 1)
    heap = [(0, start)]
    cost = 0
    max_used_dist = 0

    while heap:
        min_dist, min_node = heappop(heap)
        if visited[min_node]:
            continue

        visited[min_node] = True
        cost += min_dist
        # used_dist.append(min_dist)
        if min_dist > max_used_dist:
            max_used_dist = min_dist

        for next in graph[min_node]:
            dist = next[0]
            next_node = next[1]

            if not visited[next_node]:
                heappush(heap, (dist, next_node))

    return cost - max_used_dist


village_cnt, way_cnt = map(int, input().split())
graph = [[] for _ in range(village_cnt + 1)]

for _ in range(way_cnt):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    graph[e].append((w, s))

# visited = [False] * (village_cnt + 1)
print(prim(1))
# print(used_dist)


# s2) 크루스칼을 이용한 풀이

import sys
input = sys.stdin.readline


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


node_cnt, edge_cnt = map(int, input().split())
edges = []
for _ in range(edge_cnt):
    s, e, w = map(int, input().split())
    edges.append((w, s, e))

edges.sort()

parent = [i for i in range(node_cnt + 1)]
visited_cnt = 0
cost = 0

for dist, x, y in edges:
    x_root, y_root = find_set(x), find_set(y)

    if x_root != y_root:
        parent[y_root] = x_root
        visited_cnt += 1
        cost += dist

        if visited_cnt >= node_cnt - 2:    # 가장 큰 가중치를 제외하고 진행
            break

for idx, node in enumerate(parent):
    parent[idx] = find_set(node)

# print(parent)
print(cost)