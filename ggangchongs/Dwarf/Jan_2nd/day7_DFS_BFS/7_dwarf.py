def solution(numbers, target):
    answer = 0
    def bfs(step, number):
        nonlocal answer
        if step == len(numbers):
            if number == target:
                answer = answer + 1
            return
        bfs(step+1, number + numbers[step])
        bfs(step+1, number - numbers[step])
    
    bfs(1, numbers[0])
    bfs(1, -numbers[0])
    
    return answer
