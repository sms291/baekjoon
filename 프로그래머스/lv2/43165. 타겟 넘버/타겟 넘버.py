def solution(numbers, target):
    answer = 0
    box=[0]
    num_case=[]
    for num in numbers:
        box2=[]
        for b in box:
            box2.append(b+num)
            box2.append(b-num)
        box=box2
    answer=box.count(target)
    return answer