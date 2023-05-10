def solution(elements):
    answer = 0
    total={}
    elements2=elements*2
    for i in range(len(elements)):
        for j in range(len(elements)):
            if sum(elements2[j:i+j+1]) not in total:
                total[sum(elements2[j:i+j+1])]=0
                answer+=1
    return answer