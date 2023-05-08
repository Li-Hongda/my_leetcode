#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    ## 1.暴力遍历
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     record = []
    #     for i in range(len(strs)):
    #         find = 0
    #         if i == 0:
    #             record.append([strs[0]])
    #         else:
    #             for tmp in record:
    #                 if len(strs[i]) != len(tmp[0]) or set(tmp[0])!=set(strs[i]):
    #                     continue
    #                 num = dict()
    #                 num1 = dict()
    #                 for m in tmp[0]:
    #                     if m in num:
    #                         num[m] += 1
    #                     else:
    #                         num[m] = 1
    #                 for n in strs[i]:
    #                     if n in num1:
    #                         num1[n] += 1
    #                     else:
    #                         num1[n] = 1
    #                 if num == num1:
    #                     find = 1
    #                     tmp.append(strs[i])
    #                     break
    #             if not find:
    #                 record.append([strs[i]])
    #     return record        
    
    ## 2.借助dict 和sort快速查找
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            print(dict.get(key))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())     
# @lc code=end

