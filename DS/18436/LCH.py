import sys


def odd_merge(left, right):
    return left + right


def even_merge(left, right):
    return left + right


def odd_init(node, start, end):
    if start == end:
        odd_segtree[node] = numbers[start] % 2
        return odd_segtree[node]
    
    mid = (start + end) // 2
    left = odd_init(node*2, start, mid)
    right = odd_init(node*2+1, mid+1, end)
    odd_segtree[node] = odd_merge(left, right)
    return odd_segtree[node]


def even_init(node, start, end):
    if start == end:
        even_segtree[node] = abs(numbers[start] % 2 - 1)
        return even_segtree[node]
    
    mid = (start + end) // 2
    left = even_init(node*2, start, mid)
    right = even_init(node*2+1, mid+1, end)
    even_segtree[node] = even_merge(left, right)
    return even_segtree[node]


def odd_query(start, end, node, left, right):
    if end < left or start > right:
        return 0
    
    if start <= left and right <= end:
        return odd_segtree[node]
    
    mid = (left + right) // 2
    left_val = odd_query(start, end, node*2, left, mid)
    right_val = odd_query(start, end, node*2+1, mid+1, right)
    return odd_merge(left_val, right_val)


def even_query(start, end, node, left, right):
    if end < left or start > right:
        return 0
    
    if start <= left and right <= end:
        return even_segtree[node]
    
    mid = (left + right) // 2
    left_val = even_query(start, end, node*2, left, mid)
    right_val = even_query(start, end, node*2+1, mid+1, right)
    return even_merge(left_val, right_val)


def odd_update(index, value, node, start, end):
    if index < start or index > end:
        return odd_segtree[node]
    
    if start == end:
        odd_segtree[node] = value % 2
        return odd_segtree[node]
    
    mid = (start + end) // 2
    left = odd_update(index, value, node*2, start, mid)
    right = odd_update(index, value, node*2+1, mid+1, end)
    odd_segtree[node] = odd_merge(left, right)
    return odd_segtree[node]


def even_update(index, value, node, start, end):
    if index < start or index > end:
        return even_segtree[node]
    
    if start == end:
        even_segtree[node] = abs(value % 2 - 1)
        return even_segtree[node]
    
    mid = (start + end) // 2
    left = even_update(index, value, node*2, start, mid)
    right = even_update(index, value, node*2+1, mid+1, end)
    even_segtree[node] = even_merge(left, right)
    return even_segtree[node]


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    odd_segtree = [0] * (4 * n)
    even_segtree = [0] * (4 * n)
    odd_init(1, 0, n-1)
    even_init(1, 0, n-1)
    
    m = int(input())
    for i in range(m):
        q = list(map(int, sys.stdin.readline().split()))
        if q[0] == 1:
            odd_update(q[1]-1, q[2], 1, 0, n-1)
            even_update(q[1]-1, q[2], 1, 0, n-1)
        elif q[0] == 2:
            print(even_query(q[1]-1, q[2]-1, 1, 0, n-1))
        else:
            print(odd_query(q[1]-1, q[2]-1, 1, 0, n-1))
