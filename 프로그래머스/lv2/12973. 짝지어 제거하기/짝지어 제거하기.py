def solution (s):
# 답안 작성 부분 ===============
    answer=0
    total=[]
    for i in s:
        if not total:
            total.append(i)
        else:
            if total[-1]==i:
                total.pop()
            else:
                total.append(i)
    if len(total)==0:
        answer=1
    else:
        answer=0
   
# ==============================
    return answer