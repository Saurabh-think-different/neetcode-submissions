
from game import ConnectKGame

if __name__ == "__main__":
    rows = int(input("Enter the number of rows for the grid: "))
    cols = int(input("Enter the number of columns for the grid: "))
    k = int(input("Enter the value of K (number of consecutive pieces needed to win): "))
    target_score = int(input("Enter the target score to win the game: "))

    game = ConnectKGame(rows, cols, k, target_score)
    game.add_players()
    game.start_game()
