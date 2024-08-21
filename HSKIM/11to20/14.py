def solution(n, k, cmd):
    deleted = []
    list = [i for i in range(0, n)]

    for cmd_i in cmd:
        if cmd_i == "C":
            deleted.append(k)
            list.remove(k)

        elif cmd_i == "Z":
            restore = deleted.pop()
            list.insert(restore - 1, restore)

        else:
            action, num = cmd_i.split()
            if action == "U":
                k -= int(num)
            elif action == "D":
                k += int(num)

    result = ["O"] * n
    for i in range(len(deleted)):
        result[deleted[i]] = "X"  

    return "".join(result)

# n = 8
# k = 2
# cmd = ['D 2', 'C', 'U 3', 'C', 'D 4', 'C', 'U 2', 'Z', 'Z', 'U 1', 'C']

# print(solution(n, k, cmd))
       