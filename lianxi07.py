from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j= 0,len(nums)-1
        while i<=j:
            m = (i+j)//2
            if nums[m]<target:
                i=m+1
            elif nums[m]>target:
                j=m-1
            else:
                return m
        return -1
if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    solution = Solution()
    result = solution.search(nums, target)
    print(result)  # 输出: 4