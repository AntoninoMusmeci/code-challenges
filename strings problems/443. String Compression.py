#https://leetcode.com/problems/string-compression/
class Solution:
    def compress(self, chars: List[str]) -> int:

        i = 0
        consecutive_chars = 0
        prev_char = chars[i]
        chars.append("-")
        for c in chars:
            if c == prev_char:
                consecutive_chars += 1
            else:
                chars[i] = prev_char
                prev_char = c
                if consecutive_chars != 1:
                    for c in str(consecutive_chars):
                        i += 1
                        chars[i] = c
                consecutive_chars = 1
                i += 1
        return i