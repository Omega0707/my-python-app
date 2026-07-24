from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
          flag=[False]*9
          for j in range(9):
            if board[i][j]!='.':
                num=int(board[i][j])-1
                if flag[num]:
                    return False
                else:
                    flag[num]=True
        for j in range(9):
          flag=[False]*9
          for i in range(9):
            if board[i][j]!='.':
                num=int(board[i][j])-1
                if flag[num]:
                    return False
                else:
                    flag[num]=True
        for i in range(0,9,3):
            for j in range(0,9,3):
                flag=[False]*9
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if board[r][c]!='.':
                            num=int(board[r][c])-1
                            if flag[num]:
                                return False
                            else:
                                flag[num]=True
        return True
if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    solution = Solution()
    result = solution.isValidSudoku(board)
    print(result)  # 输出: True