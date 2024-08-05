# 배열 인덱스로 연산해서 리턴값,,
def solution(n, words):
    word_set = set()
    word_set.add(words[0])

    for i  in range(1, len(words)):
        if words[i] in word_set or words[i][0] != words[i-1][-1]:
            return [(i)%n + 1, (i)//n + 1]
        else:
            word_set.add(words[i])
    return [0, 0]

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))