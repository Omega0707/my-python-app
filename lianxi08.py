'''
6
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows== 1 or numRows >=len(s):
            return s
        Lists=[]
        Lists2=[]
        flag1=0
        flag2=True
        for _ in range(numRows):
            Lists.append([])
        for i in range(len(s)):
            if flag2==True:
                Lists[flag1].append(s[i])
                flag1+=1
                if flag1==numRows:
                   flag1-=2
                   flag2=False
            else:
                Lists[flag1].append(s[i])
                flag1-=1
                if flag1==-1:
                    flag1+=2
                    flag2=True
                else:
                    for j in range(numRows):
                        if j==flag1+1:
                            continue
                        else:
                            Lists[j].append(" ")
        for k in range(len(Lists)):
            for m in range(len(Lists[k])):
                if (Lists[k][m]!=" "):
                    Lists2.append(Lists[k][m])
        return "".join(str(x) for x in Lists2)
if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    solution = Solution()
    result = solution.convert(s, numRows)
    print(result)  # 输出: "PAHNAPLSIIGYIR"