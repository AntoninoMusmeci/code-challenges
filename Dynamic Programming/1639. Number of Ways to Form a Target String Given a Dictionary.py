#https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description/
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        target_chars = set(target)
        chars = {}
        n = len(words[0])
        for s in words:
            for j in range(n):
                if s[j] in target:
                    if s[j] not in chars:
                        chars[s[j]] = [0] * n
                    chars[s[j]][j] += 1
        
        cache = {}
        def f(start, current_pos):
            if current_pos >= len(target):
                return 1
            if (start,current_pos) in cache:
                return cache[(start, current_pos)]
            tot = 0
            char = target[current_pos]
            if char not in chars or start >= n:
                return 0
            if chars[char][start] > 0:
                tot = chars[char][start] * f(start + 1, current_pos + 1)
            tot += f(start + 1, current_pos)
            cache[(start, current_pos)] = tot
            return cache[(start, current_pos)]
        return f(0,0) %(10**9 + 7) 