class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxi = 0
        while left < right:
            water = (right - left) * min(height[right], height[left])
            if water > maxi: maxi = water
            if height[right] < height[left]: right -= 1
            else: left += 1
        return maxi
