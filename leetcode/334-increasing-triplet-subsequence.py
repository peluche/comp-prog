class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        for el in nums:
            if el <= first: first = el
            elif el <= second: second = el
            else: return True
        return False
