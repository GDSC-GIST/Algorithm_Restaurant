def solution(sizes):
    row = 0
    col = 0
    for size in sizes:
        fir = max(size)
        sec = min(size)
        if fir > row:
            row = fir
        if sec > col:
            col = sec
    answer = col * row
    return answer
