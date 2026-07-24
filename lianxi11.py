'''
34
'''
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            left,right=0,len(nums)-1
            bound=-1
            while(left<=right):
                mid=(left+right)//2
                if target>nums[mid]:
                   left=mid+1
                elif target<nums[mid]:
                   right=mid-1
                else:
                   bound=mid
                   right=mid-1
            return bound
        def findRight():
            left,right=0,len(nums)-1
            bound=-1
            while(left<=right):
                mid=(left+right)//2
                if target>nums[mid]:
                   left=mid+1
                elif target<nums[mid]:
                   right=mid-1
                else:
                   bound=mid
                   left=mid+1
            return bound
        l=findLeft()
        if (l == -1):
            return [-1, -1]
        r = findRight()
        return [l, r]
if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    solution = Solution()
    result = solution.searchRange(nums, target)
    print(result)  # 输出: [3, 4]