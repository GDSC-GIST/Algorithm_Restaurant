import sys


def merge(left, right):
    return min(left, right)


def init(tree, node, start, end):
    if start == end:
        tree[node] = numbers[start]
        return tree[node]
    
    mid = (start + end) // 2
    left = init(tree, node*2, start, mid)
    right = init(tree, node*2+1, mid+1, end)
    segtree[node] = merge(left, right)
    return segtree[node]


def update(index, value, node, start, end):
    if index < start or index > end:
        return segtree[node]
    
    if start == end:
        segtree[node] = value
        return segtree[node]
    
    mid = (start + end) // 2
    left = update(index, value, node*2, start, mid)
    right = update(index, value, node*2+1, mid+1, end)
    segtree[node] = merge(left, right)
    return segtree[node]


def query(start, end, node, left, right):
    if end < left or start > right:
        return 2000000000
    
    if start <= left and right <= end:
        return segtree[node]
    
    mid = (left + right) // 2
    left_val = query(start, end, node*2, left, mid)
    right_val = query(start, end, node*2+1, mid+1, right)
    return merge(left_val, right_val)


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    segtree = [0] * (3 * n)
    init(segtree, 1, 0, n-1)
    
    m = int(input())
    for i in range(m):
        q = list(map(int, sys.stdin.readline().split()))
        if q[0] == 1:
            update(q[1]-1, q[2], 1, 0, n-1)
        else:
            print(query(q[1]-1, q[2]-1, 1, 0, n-1))
