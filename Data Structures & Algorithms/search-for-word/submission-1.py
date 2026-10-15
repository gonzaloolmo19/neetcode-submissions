class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, board, k):
            if k == len(word):
                return True
            if i <0 or j <0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = '#'

            res = dfs(i+1, j, board, k+1) or dfs(i-1, j, board, k+1) or dfs(i, j+1, board, k+1) or dfs(i, j-1, board, k+1)
            board[i][j] = temp

            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, board, 0):
                    return True

        return False
