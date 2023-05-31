def solution(number, k):
    answer = ''
    total=[]
    cnt=0
    for idx,i in enumerate(number):
        if not total:
            total.append(i)
        else:
            if i>total[-1]:
                while(i>total[-1]):
                    total.pop()
                    cnt+=1
                    if cnt==k or (not total):
                        break 
                total.append(i)               
            else:
                total.append(i)
                pass            
            
            if cnt==k:
                break
    if cnt==k:                            
        answer=''.join(total)+number[idx+1:]
    else:
        answer=''.join(total[:-(k-cnt)])+number[idx+1:]
    return answer