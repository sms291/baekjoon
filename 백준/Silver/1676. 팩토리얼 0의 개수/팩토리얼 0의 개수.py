N=int(input())
num_dic={}
for i in range(1,N+1):
    while(i>1):
        
        cnt=0
        for k in range(2,i+1):
            if i%k==0:
                cnt=1
                i=i//k
                if k not in num_dic:
                    num_dic[k]=1
                else:
                    num_dic[k]+=1
                break
        if cnt==0:
            break
if (5 not in num_dic) or (2 not in num_dic):
    print(0)
else:
    print(min(num_dic[2],num_dic[5]))