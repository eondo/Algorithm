# 퀵 정렬
# time : 20m
# idea
'''
일반적인 퀵 정렬로서, 분배 및 분배 후의 구간의 퀵 정렬 실행 파트로 나눠 진행
'''

def apart(l, r):
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

    A[l], A[j] = A[j], A[l]
    return j


def quicksort(l, r):
    if l < r:
        m = apart(l, r)
        quicksort(l, m - 1)
        quicksort(m + 1, r)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    A = list(map(int, input().split()))

    quicksort(0, n - 1)
    # print(A)
    print(f'#{tc} {A[n // 2]}')
