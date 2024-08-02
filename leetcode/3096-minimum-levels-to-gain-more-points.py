class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        scores = [x if x else -1 for x in possible]
        total = sum(scores)
        running = 0
        for step, score in enumerate(scores[:-1]):
            running += score
            leftover = total - running
            if running > leftover:
                return step + 1
        return -1
