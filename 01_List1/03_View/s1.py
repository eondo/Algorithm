N = 10

for tc in range(1, 11):
    counts = int(input())
    heights = list(map(int, input().split()))
    counts_good_view = [0] * counts

    for i in range(2, len(heights) - 1):
        # if heights[i] > heights[i - 2] heights[i - 1] heights[i + 1] heights[i + 2]
        max_height = heights[i]
        for h in heights[i - 2 : i + 3]:
            if h > max_height:
                max_height = h

        if max_height == heights[i]: # heights[i - 2: i + 3]의 값 중 가장 max 값을 현재 max_height인 heights[i]에서 빼준다!
            max_around = heights[i - 2]
            heights_around = []

            heights_around.append(heights[i - 2])
            heights_around.append(heights[i - 1])
            heights_around.append(heights[i + 1])
            heights_around.append(heights[i + 2])

            for j in heights_around:
                if j > max_around:
                    max_around = j
            counts_good_view[i] = max_height - max_around

        else:
            counts_good_view[i] = 0

    print(f'#{tc} {sum(counts_good_view)}')