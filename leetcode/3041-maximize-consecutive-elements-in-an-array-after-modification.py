class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        dp = {} # [val] = streak
        for pos, val in enumerate(nums):
            not_inc, inc = 1, 1        
            if val - 1 in dp: not_inc = dp[val - 1] + 1
            if val in dp: inc = dp[val] + 1
            if val not in dp or not_inc > dp[val]: dp[val] = not_inc
            if val + 1 not in dp or inc > dp[val + 1]: dp[val + 1] = inc
        return max(dp.values())
