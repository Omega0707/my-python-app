class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        m,n=len(num1),len(num2)
        a=[0]*(m+n)
        for i in range(m-1,-1,-1):
            mi=ord(num1[i])-ord('0')
            isj=m-i-1
            for j in range(n-1,-1,-1):
               nj=ord(num2[j])-ord('0')
               jsj=n-j-1
               a[isj+jsj] += mi*nj
        for k in range(len(a)-1):
            a[k+1]+=a[k]//10  
            a[k]%=10
        for g in range(len(a)):
            if a[g]!=0:
              flag=g
        return "".join(str(x) for x in a[flag::-1])
if __name__ == '__main__':
    num1 = "123"
    num2 = "456"
    solution = Solution()
    result = solution.multiply(num1, num2)
    print(result)  # 输出: "56088"