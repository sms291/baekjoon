n=int(input())
total=[0,1,3]
if n==1:
    print(1)
elif n==2:
    print(3)
else:
    cnt=3
    while(cnt<=n):
        total.append(total[-2]*2+total[-1])
        cnt+=1
    print(total[-1]%10007)