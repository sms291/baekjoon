def solution(m, n, startX, startY, balls):
    answer = []
    for i in range(len(balls)):
        case=[]
        if (balls[i][0]==startX) and (balls[i][1]<startY):
            case.append(((-startX-balls[i][0])**2)+((startY-balls[i][1])**2))
            case.append(((startX-balls[i][0])**2)+((2*n-startY-balls[i][1])**2))
            case.append(((2*m-startX-balls[i][0])**2)+((startY-balls[i][1])**2)) 
        elif (balls[i][0]==startX) and (balls[i][1]>startY):
            case.append(((-startX-balls[i][0])**2)+((startY-balls[i][1])**2))
            case.append(((startX-balls[i][0])**2)+((-startY-balls[i][1])**2))
            case.append(((2*m-startX-balls[i][0])**2)+((startY-balls[i][1])**2))
        elif (balls[i][0]>startX) and (balls[i][1]==startY):
            case.append(((-startX-balls[i][0])**2)+((startY-balls[i][1])**2))
            case.append(((startX-balls[i][0])**2)+((-startY-balls[i][1])**2))
            case.append(((startX-balls[i][0])**2)+((2*n-startY-balls[i][1])**2))
        elif (balls[i][0]<startX) and (balls[i][1]==startY):
            case.append(((startX-balls[i][0])**2)+((-startY-balls[i][1])**2))
            case.append(((startX-balls[i][0])**2)+((2*n-startY-balls[i][1])**2))
            case.append(((2*m-startX-balls[i][0])**2)+((startY-balls[i][1])**2))            
        else:
            if ((startY/startX)==(balls[i][1]/balls[i][0]))|(((n-startY)/(-startX))==((n-balls[i][1])/(-balls[i][0]))):
                if ((startY/startX)==(balls[i][1]/balls[i][0])):
                    if startY>balls[i][1]:
                        case.append(((-startX-balls[i][0])**2)+((startY-balls[i][1])**2))
                        case.append(((startX-balls[i][0])**2)+((-startY-balls[i][1])**2))
                        case.append(((startX-balls[i][0])**2)+((2*n-startY-balls[i][1])**2))
                        case.append(((2*m-startX-balls[i][0])**2)+((startY-balls[i][1])**2))   
                        case.append(((2*m-startX-balls[i][0])**2)+((2*n-startY-balls[i][1])**2)) 
                        
                    else:
                        case.append(((-startX-balls[i][0])**2)+((startY-balls[i][1])**2))
                        case.append(((startX-balls[i][0])**2)+((-startY-balls[i][1])**2))
                        case.append(((startX-balls[i][0])**2)+((2*n-startY-balls[i][1])**2))
                        case.append(((2*m-startX-balls[i][0])**2)+((startY-balls[i][1])**2))   
                        case.append(((-startX-balls[i][0])**2)+((-startY-balls[i][1])**2)) 
                        
                        
                else:
                    if startY>balls[i][1]:
                        case.append(((-startX-balls[i][0])**2)+((startY-balls[i][1])**2))
                        case.append(((startX-balls[i][0])**2)+((-startY-balls[i][1])**2))
                        case.append(((startX-balls[i][0])**2)+((2*n-startY-balls[i][1])**2))
                        case.append(((2*m-startX-balls[i][0])**2)+((startY-balls[i][1])**2))  
                        case.append(((-startX-balls[i][0])**2)+((2*n-startY-balls[i][1])**2))
                    else:                    
                        case.append(((-startX-balls[i][0])**2)+((startY-balls[i][1])**2))
                        case.append(((startX-balls[i][0])**2)+((-startY-balls[i][1])**2))
                        case.append(((startX-balls[i][0])**2)+((2*n-startY-balls[i][1])**2))
                        case.append(((2*m-startX-balls[i][0])**2)+((startY-balls[i][1])**2))  
                        case.append(((2*m-startX-balls[i][0])**2)+((-startY-balls[i][1])**2))                        
                    
            else:
                case.append(((-startX-balls[i][0])**2)+((startY-balls[i][1])**2))
                case.append(((startX-balls[i][0])**2)+((-startY-balls[i][1])**2))
                case.append(((startX-balls[i][0])**2)+((2*n-startY-balls[i][1])**2))
                case.append(((2*m-startX-balls[i][0])**2)+((startY-balls[i][1])**2))            
            
            
        # case.append(((-startX-balls[i][0])**2)+((startY-balls[i][1])**2))
        # case.append(((startX-balls[i][0])**2)+((-startY-balls[i][1])**2))
        # case.append(((startX-balls[i][0])**2)+((2*n-startY-balls[i][1])**2))
        # case.append(((2*m-startX-balls[i][0])**2)+((startY-balls[i][1])**2))
        answer.append(min(case))
        print(case)
    return answer