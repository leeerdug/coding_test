def solution(array):
    answer = []
    max = 0
    index = 0
    
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            index = i
    answer.append(max)
    answer.append(index)
    
    return answer