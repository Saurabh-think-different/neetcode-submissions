
# ConnectK Grid game - with start, target_score and player mgmt (where player can choose which color to play with)
from grid import ConnectKGrid, GridCell
from player import Player

class ConnectKGame:
    def __init__(self, rows: int, cols: int, k: int = 4, target_score: int = 1):
        self._grid = ConnectKGrid(rows, cols, k)
        self._target_score = target_score
        self.players_count = 0
        self.players = {}
        self.__scores = {}

    def add_players(self):
        # All scores are 0: starting fresh, give each player a chance to select their piece
        # Ask user the number of players playing, and then for each player, ask them to select their piece color from the available colors in GridCell Enum (excluding EMPTY).

        self.players_count = int(input("Enter the number of players: "))
        available_colors = [color for color in GridCell if color != GridCell.EMPTY]
        for i in range(self.players_count):
            while True:
                player_name = input(f"Enter name for Player {i + 1}: ")
                try:
                    if player_name in self.players:
                        raise ValueError(f"Player with name {player_name} already exists. Please choose a different name.")
                    else:
                        break
                except ValueError as e:
                    print(e)
            
            self.players[player_name] = Player(player_name)

            while True:
                print(f"Available colors: {[color.name for color in available_colors]}")
                piece_choice_input = input(f"{player_name}, select your piece color from the available colors: ").upper()
                try:
                    piece_choice = GridCell[piece_choice_input]
                    self.players[player_name].select_piece(piece_choice)
                    available_colors.remove(piece_choice)  # Remove selected color from available options
                    break
                except KeyError:
                    print("Invalid color choice. Please select a valid color from the available options.")
                except ValueError as e:
                    print(e)
            

        print(f"Game started with players: {', '.join(self.players.keys())}. Target score: {self._target_score}")

    def start_game(self):
        # Implement the game loop here, where players take turns dropping pieces into the grid.
        # After each move, check for a winner and update scores accordingly.
        # The game continues until one player reaches the target score.

        current_player_index = 0
        player_names = list(self.players.keys())

        while True:
            current_player_name = player_names[current_player_index]
            current_player = self.players[current_player_name]

            print(f"\n{current_player_name}'s turn. Your piece: {current_player.piece_choice.name}")
            col = int(input(f"Enter the column (0 to {self._grid._cols - 1}) to drop your piece: "))

            try:
                row = self._grid.drop_piece(col, current_player.piece_choice)
                print(f"{current_player_name} dropped a piece in column {col}, row {row}.")
                self._grid.print_grid()
                
                if self._grid.check_winner(current_player.piece_choice):
                    print(f"{current_player_name} wins this round!")
                    current_player.set_score(current_player.score + 1)
                    print(f"{current_player_name}'s score: {current_player.score}")
                    print("WINNING GRID:")
                    self._grid.print_grid()

                    self._grid.reset_grid()
                    # View each player's score
                    print("Current scores for all players:")
                    for player in sorted(self.players.values(), key=lambda p: p.score, reverse=True):
                        print(f"{player.name}: {player.score}")

                    if current_player.score >= self._target_score:
                        print(f"{current_player_name} has reached the target score of {self._target_score} and wins the game!")
                        break
                else:
                    # Move to the next player
                    current_player_index = (current_player_index + 1) % self.players_count

            except ValueError as e:
                print(e)
        print("Game over. Thank you for playing!")