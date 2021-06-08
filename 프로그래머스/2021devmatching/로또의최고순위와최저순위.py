def solution(lottos, win_nums):
    score = {
        6:1,
        5:2,
        4:3,
        3:4,
        2:5,
        1:6,
        0:6,
    }
    answer = []
    correct = 0
    anony = 0
    for my in lottos:
        if my == 0:
            anony += 1
            continue
        if my in win_nums:
            correct += 1
    best = correct + anony
    worst = correct
    answer.append(score[best])
    answer.append(score[worst])
    return answer