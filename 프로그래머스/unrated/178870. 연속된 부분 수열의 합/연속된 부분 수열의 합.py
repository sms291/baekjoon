from collections import deque
def solution(sequence, k):
    answer = []
    total=[]
    box=deque([])
    box_len=0
    cnt=0
    start=0
    max_value=max(sequence)
    for idx,i in enumerate(sequence):
        if cnt+i<k:
            cnt+=i
            box_len+=1
            box.append(i)
        elif cnt+i>k:
            while(cnt+i>k):
                cnt-=box.popleft()
                box_len-=1
                start+=1
                if len(box)==0:
                    break       
            if cnt+i==k:              
                cnt+=i
                box_len+=1
                box.append(i)
                if box_len>1:
                    total.append([start,idx])
                else:
                    total.append([idx,idx])
                    break
                if max_value==box[0]:
                    break
            else:
                cnt+=i
                box_len+=1
                box.append(i)                
                pass         
        else:
            cnt+=i
            box_len+=1
            box.append(i)
            if box_len>1:
                total.append([start,idx])
                # if max_value==box[0]:
                #     break
            else:
                total.append([idx,idx])
                break
    answer=sorted(total,key=lambda x:(x[1]-x[0]))[0]
    return answer