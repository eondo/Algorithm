# 백준 14501. 퇴사
# time : 50m
# idea
'''

'''
def dfs(day, profit):  # day : 며칠 자 상담인지, profit : 이익
    global max_profit

    if day == n + 1:                # 모든 일자 거 다 확인했으면 끝
        if profit > max_profit:
            max_profit = profit
        return

    if plan[day][0] < n - day + 1:
        dfs(day + plan[day][0], profit + plan[day][1])

    dfs(day + 1, profit)


n = int(input())
plan = [0]
for i in range(n):
    plan.append(list(map(int, input().split())))

max_profit = 0
dfs(1, 0)

print(max_profit)