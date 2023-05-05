def solution(s):
    mun=[]
    for idx,i in enumerate(s):
        if not mun:
            mun.append(i)
        else:
            if i==mun[-1]:
                mun.pop()
            else:
                mun.append(i)
    if mun:
        answer=0
    else:
        answer=1
    return answer