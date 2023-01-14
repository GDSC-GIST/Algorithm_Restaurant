def solution(sizes):
    maxH, maxW = 0,0
    for i in sizes:
        if i[0]>=i[1]:
            maxH = max(maxH, i[0])
            maxW = max(maxW, i[1])
        else:
            maxH = max(maxH, i[1])
            maxW = max(maxW, i[0])    
    return maxH * maxW


def solution_my_edit(sizes):
    maxH, maxW = 0,0
    for h, w in sizes:
        if h < w:
            h, w = w, h
        maxH = max(maxH, h)
        maxW = max(maxW, w)    
    return maxH * maxW

def solution_best(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)