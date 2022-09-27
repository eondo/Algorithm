# 이진 탐색
# time : 2h
# idea
'''
✅ **새로 알게 된 것**
for문에서 break 되지 않으면 else로 들어가서 처리를 해주는데, 
for l in range() 안에 0 또는 -1 이 들어가는 경우에는 아예 for문이 
실행되지 않아서 break가 걸린 적이 없기 때문에 이때도 else로 들어가 
cnt가 +1 되는 현상이 발생함

🚫 **겪은 문제와 해결**
- 퀵 정렬을 쓰니까 어떻게 해도 런타임 에러가 발생 → 퀵 정렬 대신 sorted 함수 이용하니까 PASS
- 퀵 정렬을 파이써닉한 방법으로, 처음 pivot을 A[l]과 같이 처음 원소가 아니라 arr[len(arr) // 2] 로 주니까 통과하는 것을 보면 
→ 정렬하기 전 A가 이미 거의 정렬이 되어있는 꼴로 되어 있어서 처음 원소를 pivot으로 정해주면 최악의 시간복잡도일 것이라 예상됨
'''

def partition(l, r):
    i = l
    j = r
    pivot = A[l]

    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    # i, j 위치가 교차되는 때
    A[l], A[j] = A[j], A[l]
    return j


def quicksort(l, r):
    if l < r:
        middle = partition(l, r)
        quicksort(l, middle - 1)
        quicksort(middle + 1, r)


# 이진 탐색 (재귀로 구현)
def binarySearch(s, e, target, state):
    if len(state) >= 2 and state[-1] == state[-2]:
        return

    m = (s + e) // 2
    if A[m] == target:
        return state

    elif A[m] > target:
        return binarySearch(s, m - 1, target, state + ['left'])

    elif A[m] < target:
        return binarySearch(m + 1, e, target, state + ['right'])


## 이진 탐색 (반복문으로 구현)
# def binarySearch(target):
#     s = 0
#     e = n - 1
#     state = []
# 
#     while s <= e:
#         m = (s + e) // 2
# 
#         if A[m] == target:
#             return state
#         elif A[m] > target:
#             if len(state) > 0 and state[-1] == 'left':
#                 return
#             state.append('left')
#             e = m - 1
#         elif A[m] < target:
#             if len(state) > 0 and state[-1] == 'right':
#                 return
#             state.append('right')
#             s = m + 1
#         else:
#             return


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    # quicksort(0, n - 1)

    # 여기까지 리스트 A 완성!
    # 2. B 원소를 하나씩 뽑아 A에서 탐색해보기
    cnt = 0

    for k in range(m):
        target = B[k]
        if target in A:
            left_or_right = binarySearch(0, n - 1, target, [])
            # left_or_right = binarySearch(target)

            if left_or_right != None:
                for l in range(len(left_or_right) - 1):
                    if left_or_right[l] == left_or_right[l + 1]:
                        break
                else:
                    cnt += 1
                    # print('왔다갔다해서', cnt)

            ## 위의 for else로 모든 경우의 cnt를 다 다뤄줄 수 있음
            # if len(left_or_right) > 1:  # 해당 원소가 A 리스트에 있는 경우에 한 해서
            #     for l in range(len(left_or_right) - 1):
            #         if left_or_right[l] == left_or_right[l + 1]:
            #             break
            #     else:
            #         cnt += 1
            #         print('왔다갔다해서', cnt)
            #
            # if len(left_or_right) == 1:
            #     cnt += 1
            #     print(k, '1개라서', cnt)
            #
            # if not left_or_right:  # 바로 찾아서
            #     cnt += 1
            #     print('바로 찾아서', cnt)

    print(f'#{tc} {cnt}')