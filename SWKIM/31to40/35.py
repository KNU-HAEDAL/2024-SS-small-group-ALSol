def solution(n, words):
    player = [0 for _ in range(n)]  # 플레이어가 단어를 말한 횟수
    word_set = set()    # 이미 사용한 단어를 저장하는 set
    last = words[0][0]  # 이전 단어

    for idx, word in enumerate(words):
        num = idx % n
        player[num] += 1

        # 새로운 단어이며 이전 단어의 끝 알파벳으로 시작한다면
        if word not in word_set and word[0] == last[-1]:
            word_set.add(word)
            last = word
        else:
            return [num + 1, player[num]]
    
    return [0, 0]


n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))