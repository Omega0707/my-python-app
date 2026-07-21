'''
给定一个长度为 n 的 0 索引整数数组 nums。初始位置在下标 0。

每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在索引 i 处，你可以跳转到任意 (i + j) 处：

0 <= j <= nums[i] 且
i + j < n
返回到达 n - 1 的最小跳跃次数。测试用例保证可以到达 n - 1。
'''
from typing import List
class Solution:

    def jump(self,nums: List[int]) -> int:
        start=len(nums)-1
        s=0
        while (start>0):
            flag=start
            for i in range(start-1,-1,-1):
                if (i+nums[i]>=start and i<flag):
                    flag=i
            start=flag
            s+=1
        return s
if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    solution = Solution()
    result = solution.jump(nums)
    print(result)  # 输出: 2