class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = len([c for c in s[:k] if c in 'aeiou'])
        maxi = count
        for i in range(k, len(s)):
            count += (s[i] in 'aeiou') - (s[i - k] in 'aeiou')
            if count > maxi: maxi = count
        return maxi
