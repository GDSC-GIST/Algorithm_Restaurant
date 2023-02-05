import sys


def min_merge(left, right):
    return min(left, right)


def max_merge(left, right):
    return max(left, right)


def min_init(node, start, end):
    if start == end:
        min_segtree[node] = numbers[start]
        return min_segtree[node]
    
    mid = (start + end) // 2
    left = min_init(node*2, start, mid)
    right = min_init(node*2+1, mid+1, end)
    min_segtree[node] = min_merge(left, right)
    return min_segtree[node]


def max_init(node, start, end):
    if start == end:
        max_segtree[node] = numbers[start]
        return max_segtree[node]
    
    mid = (start + end) // 2
    left = max_init(node*2, start, mid)
    right = max_init(node*2+1, mid+1, end)
    max_segtree[node] = max_merge(left, right)
    return max_segtree[node]


def min_query(start, end, node, left, right):
    if end < left or start > right:
        return 2000000000
    
    if start <= left and right <= end:
        return min_segtree[node]
    
    mid = (left + right) // 2
    left_val = min_query(start, end, node*2, left, mid)
    right_val = min_query(start, end, node*2+1, mid+1, right)
    return min_merge(left_val, right_val)


def max_query(start, end, node, left, right):
    if end < left or start > right:
        return -1
    
    if start <= left and right <= end:
        return max_segtree[node]
    
    mid = (left + right) // 2
    left_val = max_query(start, end, node*2, left, mid)
    right_val = max_query(start, end, node*2+1, mid+1, right)
    return max_merge(left_val, right_val)


if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = [int(sys.stdin.readline()) for i in range(n)]
    min_segtree = [0] * (4 * n)
    max_segtree = [0] * (4 * n)
    min_init(1, 0, n-1)
    max_init(1, 0, n-1)
    
    for i in range(m):
        q = list(map(int, sys.stdin.readline().split()))
        print(min_query(q[0]-1, q[1]-1, 1, 0, n-1), \
              max_query(q[0]-1, q[1]-1, 1, 0, n-1))
