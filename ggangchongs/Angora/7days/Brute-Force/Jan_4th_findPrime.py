from itertools import permutations

def solution(numbers):
    numP = createPermutation(list(numbers))
    return checkIsPrime(numP)

def createPermutation(numList):
    numP = []
    for i in range(len(numList)):
        numP += permutations(numList,i+1)
    return numP

def checkIsPrime(numbers):
    answer = 0
    tmpNumberList = [] # for 011 11
    for strN in numbers:
        isNotPrime = False
        intN = int(''.join(s for s in strN))
        
        if intN not in tmpNumberList:
            tmpNumberList.append(intN)
            if len(strN) == 1: # 한 자리 소수는 따로 처리
                if intN == 2 or intN == 3 or intN == 5 or intN == 7:
                    answer += 1
            else:
                # 짝수인 경우는 미리 제외
                if int(strN[-1])%2 == 0: continue
                
                # 제곱근까지만 나눠보면 된다
                for i in range(3, int(intN**(1/2))+1):
                    if i%2 == 0: continue # 짝수로 나누는 경우는 제외
                    if intN%i == 0:
                        isNotPrime = True
                        break
                
                if isNotPrime == False:
                    answer += 1
    return answer

# 숫자 개수: 1~7
numbers = "1234" #3
# numbers = "011" #2

print(solution(numbers))