def solution(answers):
    pattern = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    score = [0] * 3
    for i, answer in enumerate(answers):
        for j, p in enumerate(pattern):
            if answer == p[i % len(p)]:
                score[j] += 1

    num = max(score)
    list = []
    for i in range(0, len(score)):
        if num == score[i]:
            list.append(i + 1)

    return list 
