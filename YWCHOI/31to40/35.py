def solution(n, words):
    words_set = [words[0]]

    for i in range(1, len(words) - 1):
        words_set.append(words[i])
        if words[i][-1] == words[i + 1][0]:
            if len(set(words_set)) == len(set(words)):
                continue
            else:
                return [i % n, i // n + 1]
        else:
            return [i % n, i // n + 1]
        
    return [0, 0]