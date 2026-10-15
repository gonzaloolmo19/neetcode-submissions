class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, board, remaining):
            if remaining == "":
                print("hola")
                return True
            if i <0 or j <0 or i >= len(board) or j >= len(board[0]) or board[i][j] != remaining[0]:
                return False
            
            remaining = remaining[1:]
            print(remaining, ".", board[i][j])

            temp = board[i][j]
            board[i][j] = '#'

            res = dfs(i+1, j, board, remaining) or dfs(i-1, j, board, remaining) or dfs(i, j+1, board, remaining) or dfs(i, j-1, board, remaining)
            board[i][j] = temp

            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, board, word):
                    return True

        return False
