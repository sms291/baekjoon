def solution(brown, yellow):
    # answer = []
    # total=brown+yellow
    # import math
    # if math.sqrt(total)%1==0:
    #     gil=int(math.sqrt(total))
    # else:
    #     gil=int(math.sqrt(total))+1 
    # for i in range(gil+1,0,-1):
    #     if total%i==0:
    #         width=i
    #         heigth=total//i
    #         break
    # if width<heigth:
    #     width,heigth=heigth,width
    # answer=[width,heigth]
    total=brown+yellow
    number=[]
    for i in range(1,total+1):
        if total//i<i:
            break
        if total%i==0 and (i>=3) and (total//i>=3):
            number.append(i)
    number=sorted(number,reverse=True)
    for k in number:
        if yellow==(k-2)*((total//k)-2):
            break
    answer=[total//k,k]
    return answer