#
# @lc app=leetcode id=2864 lang=python3
#
# [2864] Maximum Odd Binary Number
#

# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = s.count('1')
        return ('1'*(count-1))+('0'*(len(s)-count)) + '1'
        
# @lc code=end

