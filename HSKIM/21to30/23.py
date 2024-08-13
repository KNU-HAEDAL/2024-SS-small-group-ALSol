def solution(genres, plays):
    answer = [ ]
    genres_dic = { }
    plays_dic = { }

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if genre in genres_dic:
            genres_dic[genre] = []
            plays_dic[genre] = 0

        genres_dic[genre].append((i, play))
        plays_dic[genre] += play

    print(genres_dic, plays_dic)
    
    sorted_genres = sorted(plays_dic.items( ) , key=lambda x: x[1], reverse=True)

    # (장르, 재생 횟수) 형태의 튜플로 구성된 리스트일 때, 반복문에서 두 번째 값을 사용하지 않겠다는 의미로 _가 사용
    for genre, _ in sorted_genres:
        sorted_songs = sorted(genres_dic[genre], key=lambda x: (-x[1], x[0])) 
        # append와 달리 리스트에 여러 개의 요소를 한 번에 추가할 수 있음 
        answer.extend([i for i, _ in sorted_songs[:2]])


# g = ["classic", "pop", "classic", "classic", "pop"]
# p = [500, 600, 150, 800, 2500]

# print(solution(g, p))  
