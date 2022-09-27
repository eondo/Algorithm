# 1865. 동철이의 일 분배
# time : 1h 20m
# idea
'''
1. 직원 1번부터 N번까지 **끝까지 가봐야 결과를 얻을 수 있음** + **최대, 최소를 구하는 문제** → 완전 탐색, DFS
2. 1번 직원이 2를 선택하면 2, 3번 직원은 2를 제외한 것들 중 선택 가능하다는 것을 어떻게 구현?
    
    → `if visited[i] == 0:` 로 아직 고르지 않은 인덱스에 한 해서 for문으로 돌 수 있게 함
    
3. **visited가 [1, 1, 1]로 다 찬 후에 다른 경우를 또 고려하려면?**
    
    하나의 재귀가 끝나고 나서 visited를 원상태로 복구해주는 코드를 추가하여 모든 경우를 다 볼 수 있도록 함 (완전탐색 / 순열의 경우 참고)
'''

def find_pos(x, total, visited):    # 최대 확률을 구하는 함수(직원 인덱스, 현재까지의 확률, 방문 여부)
    global max_total                # 최대 확률 global로 선언

    if total <= max_total:      # max_total보다 작은 확률값이 나왔다면
        return                  # 해당 재귀는 종료 (1보다 작은 확률을 곱해가므로)

    if x == n:                  # 모든 직원마다 확률을 다 돌았으면
        if total > max_total:   # max_total과 비교 후 업데이트
            max_total = total
        return                  # 함수 종료

    # 아직 모든 직원의 확률을 고르지 않은 경우
    for i in range(n):          # 직원 x가 고를 수 있는 확률은 pos 인덱스 0에서 2까지
        if visited[i] == 0:     # 이미 앞에서 고른 인덱스가 아니라면
            visited[i] = 1      # 그 인덱스를 visited 처리하고
            find_pos(x + 1, total * (pos[x][i] / 100), visited) # 그 인덱스의 확률값을 곱한 값을 들고 다음 직원 처리해주러 감
            visited[i] = 0      # 위의 재귀가 끝나면 다시 visited를 되돌려줘서 모든 경우 볼 수 있도록 함


t = int(input())
for tc in range(1, t + 1):
    n = int(input())

    pos = [list(map(int, input().split())) for _ in range(n)]   # 직원마다의 성공 확률 이차원 리스트
    max_total = 0   # 최대 확률

    find_pos(0, 1, [0] * n) # 0번 직원부터, 초기 확률 1을 들고, 아직 visited가 다 0인 상태로 함수 실행!
    print(f'#{tc} {100 * max_total:.6f}')   # 출력 형태 소수점 6자리까지 무조건 나오도록 함