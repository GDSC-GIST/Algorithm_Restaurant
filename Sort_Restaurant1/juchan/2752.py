import sys

input = sys.stdin.readline

nums = list(map(int, input().split()))

nums.sort()
print(*nums) # *을 붙이면 리스트의 요소들을 하나씩 출력