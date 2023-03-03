# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(needle)
        h = len(haystack)
        if h < n:
            return -1
        lps = [0] * n
        prev = 0
        i = 1
        while i < n:
            if needle[i] == needle[prev]:
                prev += 1
                lps[i] = prev
                i += 1
            else:
                if prev == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prev = lps[prev-1]
        i = 0
        j = 0
        print(lps)
        h_pointer = 0
        n_pointer = 0
        while h_pointer < h:
            if needle[n_pointer] == haystack[h_pointer]:
                h_pointer += 1
                n_pointer += 1
                if n == n_pointer:
                    return h_pointer - n
            else:
                if n_pointer == 0:
                    h_pointer += 1
                else:
                    n_pointer = lps[n_pointer - 1]

        return -1


#
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         h = len(haystack)
#         n = len(needle)
#         if  n == 0:
#             return 0
#         if n > h:
#             return -1
#         i = 0
#         while i <= h-n:
#             j = 0
#             while j < n:
#                 if haystack[i + j] != needle[j]:
#                     break
#                 j += 1
#             if j == n:
#                 return i
#             i += 1
#         return -1
#
#  O(h*n)
