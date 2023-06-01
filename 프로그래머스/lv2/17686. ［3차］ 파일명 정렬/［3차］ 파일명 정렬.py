def solution(files):
# 답안 작성 부분 ===============
    answer=[]
    total=[]
    for file in files:
        head=''
        number=''
        tail=''
        cnt=0
        for idx,text in enumerate(file):
            if not text.isdigit():
                head+=text
            else:
                break
        file=file[idx:]
        knt=0
        for idx,text in enumerate(file):
            if text.isdigit() and idx<5:
                number+=text
            else:
                knt=1
                break
        if knt==1:
            tail=file[idx:]
        else:
            pass
    
        total.append([head,number,tail])
      #print(total)  
    for i in sorted(total,key=lambda x:[x[0].upper(),x[1].zfill(5)]):
        answer.append(''.join(i))
    return answer
