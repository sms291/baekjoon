def solution(numbers):
    answer = []
    for i in numbers:
        if bin(i)[-1]=='0':
            answer.append(i+1)
        else:
            if '0' not in bin(i)[2:]:
                if i==1:
                    answer.append(2)
                elif i==3:
                    answer.append(5)
                else:
                    answer.append(int('10'+'1'*(len(bin(i)[2:])-1),2))
            
            else:
                num=''
                for idx,k in enumerate(bin(i)[-1:1:-1],1):
                    if k=='1':
                        num+='1'
                    else:
                        num='1'*(len(num)-1)+'01'+bin(i)[-(idx+1):1:-1]
                        break

                answer.append(int(num[::-1],2))
    return answer