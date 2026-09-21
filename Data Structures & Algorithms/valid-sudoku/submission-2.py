class Solution:

    def transform(self, board, simple=True):
        transformed_board = [[None]*len(row) for row in board]

        if simple:
            for i, row in enumerate(board):
                for j in range(len(row)):
                    transformed_board[j][i] = row[j]
        else:
            for square in range(9):
                k = 0
                for i in range(3):
                    for j in range(3):
                        row = (square//3) * 3 + i
                        col = (square%3) * 3 + j
                        transformed_board[square][k] = board[row][col]
                        k+=1
        return transformed_board

    def validate_rows(self, board):
        for row in board:
            seen = set()
            for i in row:
                if i != "." and i in seen:
                    return False
                seen.add(i)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row validation
        if not self.validate_rows(board):
            return False
        
        # Column validation
        board_transformed = self.transform(board)
        if not self.validate_rows(board_transformed):
            return False

        # square validation
        board_transformed = self.transform(board, simple=False)
        if not self.validate_rows(board_transformed):
            return False

        return True