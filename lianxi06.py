'''
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。
'''
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        list1=[0]*n
        list2=[0]*n
        m=0
        for i in range(n):
            list1[i]=i+1
            list2[i]=i+1
        while(m<n-1):
            s=k//math.factorial(n-m-1)
            y=k%math.factorial(n-m-1)
            k=y
            if (y==0):
                list1[m]=list2[s-1]
                del list2[s-1]
                list2.sort(reverse=True)
                list1=list1[0:n-len(list2)]
                list1+=list2
                break
            else:
                list1[m]=list2[s]
                del list2[s]
            m+=1

        return "".join(str(x) for x in list1)
if  __name__ == '__main__':
    n = 3
    k = 3
    solution = Solution()
    result = solution.getPermutation(n, k)
    print(result)  # 输出: "213"