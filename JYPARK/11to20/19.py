def solution(string_list, query_list):
    answer = [False] * len(query_list)
    for i in range(len(query_list)):
        if query_list[i] in string_list:
            answer[i] = True
    return answer

string_list = ["apple", "banana", "cherry"]
query_list = ["banana", "kiwi", "melon", "apple"]
print(solution(string_list, query_list))