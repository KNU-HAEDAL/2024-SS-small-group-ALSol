def polyhash(str):
    p = 21
    m = 1_000_000_007
    hashvalue = 0

    for char in str:
        hashvalue = (hashvalue * p + ord(char)) % m
    
    return hashvalue


def solution(participant, completion):
    incompletion = ""
    hashtable = [polyhash(str) for str in participant]

    for complete in completion:
        complete_hash = polyhash(complete)
        if complete_hash in hashtable:
            hashtable.remove(complete_hash)

    if hashtable:
        incomplete_hash = hashtable[0]
        for participant_str in participant:
            if polyhash(participant_str) == incomplete_hash:
                incompletion = participant_str
                break

    return incompletion