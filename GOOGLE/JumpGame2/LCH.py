# 14269ms, 15MB, 0
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] + [99999] * (len(nums) - 1)
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                index = min(i+j, len(nums) - 1)
                dp[index] = min(dp[index], dp[i] + 1)
        return dp[-1]
