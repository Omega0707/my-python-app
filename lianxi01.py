'''
给你一个字符串 s，找到 s 中最长的 回文子串。
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def calculate(s, left, right):
            flag = True
            if right >= len(s):
                return 0
            if (s[left] == s[right]):
                sum = right - left + 1
            else:
                return 0
            while (flag and left > 0 and right < len(s) - 1):
                if (s[left - 1] == s[right + 1]):
                    sum += 2
                    left -= 1
                    right += 1
                else:
                    flag = False
            return sum

        maxl, start = 0, 0
        for i in range(len(s)):
            len1 = calculate(s, i, i)
            len2 = calculate(s, i, i + 1)

            if (maxl < max(len1, len2)):
                maxl = max(len1, len2)
                start = i - (maxl - 1) // 2
        return s[start:start + maxl]
if __name__ == '__main__':
    s = "babad"
    solution = Solution()
    result = solution.longestPalindrome(s)
    print(result)  # 输出: "bab" 或 "aba"