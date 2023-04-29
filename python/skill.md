# 双指针
## 快慢指针
### 26&&80
定义两个指针`left`和`right`，`right`从左到右把所有元素扫一遍，将不重复的元素赋给`left`的下一位.
## 摩尔投票
取巧解法:题目中假定一定存在大于一半的数字，所以列表中间位置一定是那个数字。
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)//2
        return nums[l] 
```



