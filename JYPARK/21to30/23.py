def solution(genres, plays):
    answer = []
    hash_table = { }
    count_play = { }
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in hash_table:
            hash_table[genre] = [ ]
            count_play[genre] = 0
        hash_table[genre].append((i, play))    #순서유지위해 튜플사용. {} -> set만든다
        count_play[genre] += play

    #총 재생 횟수가 많은 장르순으로 정렬
    sorted_genre = sorted(count_play.items(), key = lambda x : x[1], reverse = True)

    #장르별 재생 횟수가 많은 노래순으로 정렬
    for genre, _ in sorted_genre:
        sorted_songs = sorted(hash_table[genre], key = lambda x : (-x[1], x[0]))    #x[0] -> 재생횟수가 같다면, 인덱스 기준 오름차순 정렬
        answer.extend(j for j, _ in sorted_songs[0:2])                              #-x[1] -> 재생 횟수 기준 내림차순 정렬
        
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))