def solution(genres, plays):
    answer = []
    music = {}  # 각 장르의 인덱스와 play를 저장하는 dict
    record = {} #  각 장르의 play 총합을 저장하는 dict
    idx = 0

    # music의 vlaue 값을 2차원 배열로 저장하며 저장되는 방식은 [index, play]
    # record에는 각 장르에 맞는 play를 더해 총합을 구하는 방식
    for g, p in zip(genres, plays):
        if g in music:
            music[g].append([idx, p])
            record[g] += p
        else:
            music[g] = [[idx, p]]
            record[g] = p
        
        idx += 1
    
    # play 총합을 기준으로 장르를 내림차순으로 정렬
    sorted_genres = sorted(record, key= lambda x: record[x], reverse=True)

    # 장르에 속한 곡이 하나일 경우와 2개 이상인 경우를 구분
    for i in sorted_genres:
        if len(music[i]) < 2: # 장르에 속한 곡이 하나일 경우 정렬하지 않고 바로 추가
            first = music[i][0]
            answer.append(first[0])
        else:   # 장르에 속한 곡이 2개 이상일 때 play를 기준으로 내림차순 정렬 진행
            music[i] = sorted(music[i], key= lambda x: x[1], reverse=True)
            
            first = music[i][0]
            second = music[i][1]

            answer.append(first[0])
            answer.append(second[0])

    return answer  
    
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

