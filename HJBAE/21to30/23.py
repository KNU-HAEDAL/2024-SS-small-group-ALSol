"""
장르별로 가장 많이 재생된 노래를 2개씩 모아 베스트 앨범 출시
속한 노래가 많이 재생된 장르를 먼저 수록
장르 내에서 많이 재생된 노래를 먼저 수록
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록

genres[i]는 고유 번호가 i인 노래의 장르
plays[i]는 고유 번호가 i인 노래가 재생된 횟수
장르에 속한 곡이 하나라면, 하나의 곡만 선택
"""

def solution(genres, plays):
    genres_list = {}    # 장르 + 재생 횟수 정리
    playlist = {}    # 전체 플레이리스트 종류

    for i in range(len(genres)):
        if genres[i] not in genres_list:
            genres_list[genres[i]] = plays[i]
            playlist[genres[i]] = [(i, plays[i])]
        else:
            genres_list[genres[i]] += plays[i]
            playlist[genres[i]].append((i, plays[i]))
    # playlist[genres[i]].append((i, plays[i]))
    # 이러면 장르별 총합은 일단 구해짐 -> 정렬

    sorted_genres = sorted(genres_list.items(), key = lambda x : x[1], reverse = True)

    best_list = []    # 답안 내용 들어갈 리스트
    
    for genre, _ in sorted_genres:
        sorted_songs = sorted(playlist[genre], key = lambda x : (-x[1], x[0]))
        best_list.extend([song[0] for song in sorted_songs[:2]])

    return best_list

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# return = [4, 1, 3, 0]

print(solution(genres, plays))

# lambda 말고 operator 모듈의 itemgetter 사용도 가능하다고 하네요
# lambda 사용법 재숙지 필요할듯