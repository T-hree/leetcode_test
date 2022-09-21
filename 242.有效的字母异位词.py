#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     ss = list(s)
    #     tt = list(t)
    #     ss.sort()
    #     tt.sort()
    #     return ss == tt
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(list(s)) == sorted(list(t))
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for i in s:
            # if i not in dict1:
            #     dict1[i] = 1
            # else:
            #     dict1[i] += 1
            dict1[i] = dict1.get(i,0) + 1
        for i in t:
            # if i not in dict2:
            #     dict2[i] = 1
            # else:
            #     dict2[i] += 1
            dict2[i] = dict2.get(i,0) + 1
        return dict1 == dict2
# @lc code=end

