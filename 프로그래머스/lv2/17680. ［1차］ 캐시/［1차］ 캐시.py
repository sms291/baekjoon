def solution(cacheSize, cities):
    answer = 0
    dict1={}
    dict2={}
    for idx,i in enumerate(cities):
        if i.upper() not in dict1:
            answer+=5
            dict1[i.upper()]=idx
            dict2[idx]=i.upper()
            if len(dict1)>cacheSize:
                minimum=dict2[min(dict2.keys())]
                del dict1[minimum]
                del dict2[min(dict2.keys())]
        else:
            answer+=1
            org_num=dict1[i.upper()]
            dict1[i.upper()]=idx
            dict2[idx]=i.upper()
            del dict2[org_num]
    print(dict1)
    print(dict2)
    return answer