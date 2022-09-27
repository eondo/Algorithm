# 전기버스 2
# time : 40m
# idea
'''
현재 가진 배터리로 갈 수 있는 모든 특정 정류소에서 충전하는 경우 모든 것을 다 고려 후, 가지치기 진행하기
→ DFS + charge_cnt 기준으로 가지치기
'''

def charge_times(s, cnt):   # 최소 충전 횟수를 찾는 함수
    global min_cnt          # 현재까지의 최소 충전 횟수

    if cnt >= min_cnt:      # 가치지기 : 이미 현재의 최소를 넘은 경우
        return              # 해당 재귀를 종료

    if s >= n - 1:          # 종점에 도착했다면 (현재 위치 s가 종점 인덱스 이상)
        if cnt < min_cnt:   # min_cnt 업데이트
            min_cnt = cnt
        return min_cnt

    avail = charge[s]       # 아직 진행 중이라면 해당 위치에서의 연료를 확인하고
    for i in range(1, avail + 1):       # 그 연료만큼 갈 수 있는 모든 정류장들에 대하여
        charge_times(s + i, cnt + 1)    # 그 정류장을 시작점으로 갈 수 있는 정류장들 탐색을 재귀로 진행


t = int(input())
for tc in range(1, t + 1):
    info = list(map(int, input().split()))
    n = info[0]         # 정류장 개수
    charge = info[1:]   # 정류장마다 연료의 양 정보
    min_cnt = len(charge)   # 초기 최소 충전수

    charge_times(0, 0)  # 0 인덱스에서 출발, 아직 충전횟수는 0으로 함수를 시작

    print(f'#{tc} {min_cnt - 1}')