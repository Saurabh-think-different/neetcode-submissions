
from grid import GridCell

class Player:
    def __init__(self, name):
        self._name = name
        self._piece_choice = None # can choose any color from GridCell Enum
        self._score = 0

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score
    
    @property
    def piece_choice(self):
        return self._piece_choice

    @name.setter # incase they wish to change their name
    def name(self, value):
        self._name = value
    
    def select_piece(self, piece_choice):
        if not isinstance(piece_choice, GridCell) or piece_choice == GridCell.EMPTY:
            raise ValueError("Invalid piece choice. Must be a non-empty GridCell.")
        if self._piece_choice is not None:
            raise ValueError(f"Piece choice already selected. You have to stick with {self._piece_choice.name}.")

        self._piece_choice = piece_choice
        print(f"{self._name} selected {self._piece_choice.name} as their piece.")

    def set_score(self, score):
        if not isinstance(score, int) or score < 0:
            raise ValueError("Score must be a non-negative integer.")
        self._score = score