'''
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
'''
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        for i in range(n):
            for j in range(0,n-i-1):
                if (intervals[j][0]>intervals[j+1][0]):
                    intervals[j],intervals[j+1]=intervals[j+1],intervals[j]
        j=0
        while(j<n-1):
            if intervals[j][1]>=intervals[j+1][0]:
                intervals[j][1]=max(intervals[j+1][1],intervals[j][1])
                #intervals=intervals[:j+1]+intervals[j+2:]
                del intervals[j+1]
                n-=1
                j-=1
            j+=1
        return intervals
if __name__=='__main__':
    intervals=[[1,3],[2,6],[8,10],[15,18]]
    solution=Solution()
    result=solution.merge(intervals)
    print(result)  # 输出: [[1,6],[8,10],[15,18]]