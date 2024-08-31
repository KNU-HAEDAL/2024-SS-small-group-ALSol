def solution(blue,white):
    total=blue+white
    for vertical in range(3,int(total**0.5)+1):
        if total% vertical==0:
            horizontal=(int)(total/vertical)
            if blue==(horizontal+vertical-2)*2:
                return [horizontal,vertical]
    return[]