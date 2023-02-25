# 9574ms, 18.2MB, -3
# ^ cool!
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 1):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    if not temp in ans:
                        ans.append(temp)
                if sum3 < 0:
                    j += 1
                else:
                    k -= 1
        return ans
