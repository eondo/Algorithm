# SWEA 1251. 하나로

from heapq import heappush, heappop


def prim(idx):                      # prim(idx = 시작점 섬의 인덱스를 인자로 받음)
    visited = [False] * (land_cnt)  # 섬의 번호 대신 섬의 인덱스 값으로 visited 처리
    heap = [(0, idx)]               # 시작점 섬의 w와 인덱스를 튜플로 묶은 heap
    cost = 0                        # 초기 비용

    while heap:
        min_dist, min_idx = heappop(heap)   # 가장 작은 w와 그때의 idx를 가져옴
        if visited[min_idx]:                # 그 idx가 이미 방문한 인덱스 값이라면
            continue                        # 볼 필요 없음
            
        visited[min_idx] = True             # 아직 방문 안 했으면 방문 처리를 True로 해주고
        cost += min_dist                    # 해당 인덱스의 섬을 잇는 비용을 더함

        for i in range(land_cnt):           # 모든 섬에 접근 가능하므로 모든 섬 인덱스에 대하여
            next_idx = i                    # 그 섬의 인덱스를 next_idx에 저장
            # next_node_x = land_x[i]
            # next_node_y = land_y[i]
            
            # 현재 위치(min_idx)와 선택된 다음 next_idx 번호의 섬 사이의 w 구함
            dist = e * ((land_x[min_idx] - land_x[next_idx]) ** 2 + (land_y[min_idx] - land_y[next_idx]) ** 2)

            if not visited[next_idx]:               # next_idx가 아직 방문 안 한 섬의 인덱스라면
                heappush(heap, (dist, next_idx))    # heap에 해당 w와, 그 인덱스를 저장

    return cost

t = int(input())
for tc in range(1, t + 1):
    land_cnt = int(input())                     # 섬의 개수
    land_x = list(map(int, input().split()))    # 섬의 x 좌표들 리스트
    land_y = list(map(int, input().split()))    # 섬의 y 좌표들 리스트
    e = float(input())                          # 세율

    print(f'#{tc} {round(prim(0))}')