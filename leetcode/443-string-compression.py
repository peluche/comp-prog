class Solution:
    def compress(self, chars: List[str]) -> int:
        last = chars[0]
        pos, count = 0, 0
        for el in chars + [None]:
            if el == last: count += 1
            else:
                chars[pos] = last
                pos += 1
                if count > 1:
                    for digit in str(count):
                        chars[pos] = digit
                        pos += 1
                last = el
                count = 1
        return pos
