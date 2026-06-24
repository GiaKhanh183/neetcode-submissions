class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        substring = set()
        longestsubstring = 0

        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1

            substring.add(s[r])
            longestsubstring = max(longestsubstring, r - l + 1)

        return longestsubstring