def solution(operations):
    answer=[]
    for i in range(len(operations)):
        if not answer:
            if 'I' in operations[i]:
                answer.append(int(operations[i].split(' ')[-1]))
            else:
                pass
        else:
            if 'I' in operations[i]:
                answer.append(int(operations[i].split(' ')[-1]))
            else:
                if 'D' in operations[i]:
                    #print(operations[i].split(' '))
                    if '1'==operations[i].split(' ')[-1]:
                        max_num=answer.index(max(answer))
                        answer.pop(max_num) 
                    else:
                        #print(answer)
                        #print(min(answer))
                        min_num=answer.index(min(answer))
                        answer.pop(min_num) 
        #print(answer)
    
    if not answer:
        answer=[0,0]
    else:
        answer=[max(answer),min(answer)]    
    return answer