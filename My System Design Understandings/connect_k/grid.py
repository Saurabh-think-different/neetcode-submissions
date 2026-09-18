
import enum

# Multiplayer - Royale style game

class GridCell(enum.Enum):
    EMPTY = 0
    RED = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4
    ORANGE = 5
    PURPLE = 6
    WHITE = 7
    BLACK = 8

class ConnectKGrid:

    def __init__(self, rows: int, cols: int, k: int):
        self._rows = rows
        self._cols = cols
        self._k = k
        self._grid = [[GridCell.EMPTY for _ in range(cols)] for _ in range(rows)]

    def get_grid(self):
        return self._grid
    
    def drop_piece(self, col: int, piece: GridCell):
        if col < 0 or col >= self._cols:
            raise ValueError("Column index is out of bounds. Invalid piece drop.")
        if piece is GridCell.EMPTY:
            raise ValueError("Cannot drop an empty piece.")
        for row in reversed(range(self._rows)):
            if self._grid[row][col] == GridCell.EMPTY:
                self._grid[row][col] = piece
                print(f"Dropped {piece.name} piece in column {col}, row {row}.")
                return row
        raise ValueError("Column is full. Invalid piece drop.")

    def check_winner(self, piece: GridCell) -> bool:
        if piece is GridCell.EMPTY:
            raise ValueError("Cannot check for an empty piece.")
        
        is_winner = False
        # horizontal check
        for row in range(self._rows):
            count = 0
            for col in range(self._cols):
                if self._grid[row][col] == piece:
                    count += 1
                    if count >= self._k:
                        is_winner = True
                        break
                else:
                    count = 0
                if is_winner:
                    break
        
        # vertical check
        for col in range(self._cols):
            count = 0
            for row in range(self._rows):
                if self._grid[row][col] == piece:
                    count += 1
                    if count >= self._k:
                        is_winner = True
                        break
                else:
                    count = 0
            if is_winner:
                break
        
        # normal diagonal check
        for row in range(self._rows - self._k + 1):
            for col in range(self._cols - self._k + 1):
                count = 0
                for i in range(self._k):
                    if self._grid[row + i][col + i] == piece:
                        count += 1
                    else:
                        break
                if count >= self._k:
                    is_winner = True
                    break
            if is_winner:
                break

        # anti diagonal check
        for row in range(self._rows - self._k + 1):
            for col in range(self._cols - self._k + 1):
                count = 0
                for i in range(self._k):
                    if self._grid[row + i][col - i] == piece:
                        count += 1
                    else:
                        break
                if count >= self._k:
                    is_winner = True
                    break
            if is_winner:
                break

        return is_winner
        
    def is_full(self):
        return all(cell != GridCell.EMPTY for row in self._grid for cell in row)

    def reset_grid(self):
        self._grid = [[GridCell.EMPTY for _ in range(self._cols)] for _ in range(self._rows)]
        print("Grid has been reset.")

    def print_grid(self):
        for row in self.get_grid():
            print(' | '.join(str(cell.name) for cell in row))
            print('-' * (self._cols * 4 - 1))
