import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    result = 0

    for i in range(n): ## 기준점에 대한 반복
        max_height = 0

        for j in range(i + 1, n):
            if numbers[i] > numbers[j]: ## 기준점에 대한 오른쪽 박스기둥의 반복
                max_height += 1

        if result < max_height:
            result = max_height

    print(f'#{tc} {result}')