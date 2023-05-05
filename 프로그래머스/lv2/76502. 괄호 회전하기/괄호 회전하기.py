def solution(s):
    answer = 0
    number=0
    while(len(s)-1>=number):
        mun=[]
        
        for idx,i in enumerate(s):
            if not mun:
                mun.append(i)
            else:
                if (mun[-1]=='[') and (i==']'):
                    mun.pop()
                elif (mun[-1]=='{') and (i=='}'):
                    mun.pop()
                elif (mun[-1]=='(') and (i==')'):
                    mun.pop()
                else:
                    mun.append(i)
        if not mun:
            answer+=1
        s=s[1:]+s[0]
        number+=1
    return answer