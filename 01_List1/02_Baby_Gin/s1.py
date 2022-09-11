N = int(input())

for tc in range(1, N + 1):
    cards = list(map(int, list(input()))) ## list(map(int, input().split()))
    cards_counts = [0] * 12

    print(cards)

    baby_gin = 0
    baby_gin_bool = 0

    # cards의 값을 index로, 해당 값의 개수를 value로 갖는 리스트 완성
    for i in cards:
        cards_counts[i] += 1

    print(cards_counts)
    j = 0
    k = 0
    # triplet 검사
    while j < 10:
        if cards_counts[j] >= 3:
            baby_gin += 1
            cards_counts[j] = cards_counts[j] - 3  ## 해당 값을 triplet 수 없앤 값으로 초기화
            continue
        j += 1

    # run 검사
    # for k in range(len(cards_counts)): ## [..., 2, 2, 2, ...]인 경우에도 괜찮은가? 아니. 안된다. 한 번 더 돌아야 할 것 같은데?
    while k < 10:
        if cards_counts[k] >= 1 and cards_counts[k + 1] >= 1 and cards_counts[k + 2] >= 1:
            cards_counts[k] -= 1
            cards_counts[k + 1] -= 1
            cards_counts[k + 2] -= 1

            baby_gin += 1
            continue
        k += 1

    if baby_gin == 2:
        baby_gin_bool = 1
    else:
        baby_gin_bool = 0

    print(f'#{tc} {baby_gin_bool}')

