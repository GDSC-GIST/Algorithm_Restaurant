# not yet

def solution(phone_book):
    answer = True
    if len(phone_book) == 1: return answer
    
    phone_book.sort()
    for i in range(1, len(phone_book)):
        candi = phone_book[i-1]
        if phone_book[i][:len(candi)] == candi:
            return False
    
    return answer


phone_book = ["119", "97674223", "1195524421"]
phone_book = ["123","456","789", "1256", "1313123", "123456789"]
phone_book = ["6", "12", "6789"]
phone_book = ["12","123","1235","567","88"]
# phone_book = ["123", "3123"]

phone_book.sort()
print(phone_book)



def solution_old(phone_book):
    answer = True
    if len(phone_book) == 1: return answer
    
    phone_book = sorted(phone_book, key=lambda x: len(x))
    phoneDict = {}
    phoneDict[phone_book[0]] = len(phone_book[0])
    # key = phone number
    # value = len(phone number)
    lenList = [len(phone_book[0])]
    
    for i in range(1, len(phone_book)):
        for j in lenList:
            if phone_book[i][:j] not in phoneDict:
                phoneDict[phone_book[i]] = len(phone_book[i])    
            else:
                return False
        if len(phone_book[i]) not in lenList:
            lenList.append(len(phone_book[i]))
    return answer