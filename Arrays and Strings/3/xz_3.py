class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        mp = set()
        left = 0
        for right in range(n):
            while s[right] in mp:
                mp.remove(s[left])
                left += 1
            mp.add(s[right])
            
            ans = max(ans, right - left + 1)
        return ans
    
