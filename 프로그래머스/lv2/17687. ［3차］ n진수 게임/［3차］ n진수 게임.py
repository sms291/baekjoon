def solution(n, t, m, p):
    answer = ''
    total=''
    for i in range(p+m*t):
        su=i
        if su<=1:
            total+=str(i)
        else:
            jinsu=''
            while(su>1):
                #print(su)
                mok=su//n
                namu=su%n
                su=mok
                # if mok<n:
                #     break
                # else:
                #     pass
                if namu==10:
                    jinsu='A'+jinsu
                elif namu==11:
                    jinsu='B'+jinsu
                elif namu==12:
                    jinsu='C'+jinsu
                elif namu==13:
                    jinsu='D'+jinsu
                elif namu==14:
                    jinsu='E'+jinsu
                elif namu==15:
                    jinsu='F'+jinsu
                else:
                    jinsu=str(namu)+jinsu     
                if su<n:          
                    if mok==10:
                        jinsu='A'+jinsu
                    elif mok==11:
                        jinsu='B'+jinsu
                    elif mok==12:
                        jinsu='C'+jinsu
                    elif mok==13:
                        jinsu='D'+jinsu
                    elif mok==14:
                        jinsu='E'+jinsu
                    elif mok==15:
                        jinsu='F'+jinsu
                    else:
                        if mok!=0:
                            jinsu=str(mok)+jinsu 
                        
                    break 
            total+=jinsu
        #total+=jinsu            
    answer=total[p-1::m][:t]
    
    return answer