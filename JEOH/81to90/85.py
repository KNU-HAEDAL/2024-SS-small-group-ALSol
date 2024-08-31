def solution(N, stations, Y):
    answer = 0
    location = 1 
    idx = 0 
    while location <= N:
        if idx < len(stations) and location >= stations[idx] - Y: 
            location = stations[idx] + Y  + 1
            idx += 1
        else:
            location += 2 * Y + 1
            answer += 1 
    return answer