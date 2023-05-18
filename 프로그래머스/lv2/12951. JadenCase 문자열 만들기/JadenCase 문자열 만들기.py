def solution(s):
# 답안 작성 부분 ===============
    total=[]
    for i in s.split(" "):
        if i!='' and i[0].isalpha():
            total.append(i[0].upper() + i[1:].lower())
        else:
            total.append(i.lower())
    answer=' '.join(total)
# ==============================
    return answer