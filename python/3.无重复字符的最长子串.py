#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        start = 0
        a = dict()
        for end in range(len(s)):
            a[s[end]] = a.get(s[end], 0) + 1
            if len(a) == end - start + 1:
                maxlen = max(maxlen, end - start + 1)
            
            while end-start+1 > len(a):
                head = s[start]
                a[head] -= 1
                if a[head] == 0:
                    del a[head]
                start +=1
        return maxlen




# @lc code=end


