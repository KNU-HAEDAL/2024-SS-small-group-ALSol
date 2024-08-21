"""
1부터 n까지 번호가 붙어 있는 n명의 사람이 영어 끝말잇기 함
1. 1번부터 번호 순서대로 한 사람씩 단어를 말함
2. 마지막 사람이 단어를 말한 다음 다시 1번부터 시작
3. 앞 사람이 말한 단어의 마지막 문자로 시작하는 단어
4. 이전에 등장헀던 단어 사용 X
5. 한 글자인 단어 X
가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째에 탈락했는지 반환하는 solution()
"""
def solution(n, words):
    used_words = set()    # 사용한 단어 집합
    previous_word = words[0][0]

    for i, word in enumerate(words):
        # 단어가 이미 사용한 단어 OR 단어 첫 글자(인덱스 0)이 전 단어 끝 글자(인덱스 -1)이랑 다른 경우
        if word in used_words or word[0] != previous_word[-1]:
            person = (i % n) + 1
            turn = (i // n) + 1
            return [person, turn]
        
        used_words.add(word)
        previous_word = word
    
    return [0, 0]


n1 = 3
words1 = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
# result1 = [3, 3]
print(solution(n1, words1))

n2 = 5
words2 = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
# result2 = [0, 0]
print(solution(n2, words2))

n3 = 2
words3 = ["hello", "one", "even", "never", "now", "world", "draw"]
# result3 = [1, 3]
print(solution(n3, words3))