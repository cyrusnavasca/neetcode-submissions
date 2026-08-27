class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_rows, n_cols = len(board), len(board[0])
        path = set()

        def backtrack(row, col, i):
            # when do we need to exit
            if i == len(word):
                return True
            if row < 0 or row >= n_rows or col < 0 or col >= n_cols or (row,col) in path or word[i] != board[row][col]:
                return False
            
            # traversal 
            path.add((row,col))
            res = (backtrack(row+1, col, i+1) or # right
            backtrack(row-1, col, i+1) or # left
            backtrack(row, col+1, i+1) or # up
            backtrack(row, col-1, i+1)) # down
            path.remove((row,col))

            return res
        
        for row in range(n_rows):
            for col in range(n_cols):
                if backtrack(row, col, 0):
                    return True
                
        return False

        