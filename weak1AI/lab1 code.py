Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
from copy import deepcopy

... class TicTacToeNode:
...     def __init__(self, board, current_player='1', path_cost=0, parent=None):
...         self.board = board  # 3x3 grid: '0', '1', or ' '
...         self.current_player = current_player
...         self.path_cost = path_cost  # Cumulative path cost (depth in tree)
...         self.parent = parent
... 
...     def is_game_over(self):
...         """Checks if a player has won or if the board is full."""
...         b = self.board
...         lines = (
...             # Rows & Columns
...             [b[i] for i in range(3)] + [[b[r][c] for r in range(3)] for c in range(3)] +
...             # Diagonals
...             [[b[0][0], b[1][1], b[2][2]], [b[0][2], b[1][1], b[2][0]]]
...         )
...         for line in lines:
...             if line[0] != ' ' and line[0] == line[1] == line[2]:
...                 return True, f"Player '{line[0]}' Won"
...         
...         if all(cell != ' ' for row in b for cell in row):
...             return True, "Draw"
...             
...         return False, None
... 
...     def get_legal_next_states(self, move_cost=1):
...         """Generates all legal next states and updates the path cost."""
...         game_over, _ = self.is_game_over()
...         if game_over:
...             return []  # No legal moves if game has ended
... 
...         next_states = []
...         next_player = '0' if self.current_player == '1' else '1'
... 
...         for r in range(3):
...             for c in range(3):
...                 if self.board[r][c] == ' ':
...                     # Create a deep copy of the board and apply move
...                     new_board = deepcopy(self.board)
...                     new_board[r][c] = self.current_player
...                     
...                     # Calculate new path cost: current path cost + cost of step
...                     new_path_cost = self.path_cost + move_cost
...                     
...                     child_node = TicTacToeNode(
...                         board=new_board,
...                         current_player=next_player,
...                         path_cost=new_path_cost,
...                         parent=self
...                     )
...                     next_states.append(child_node)
... 
...         return next_states
... 
...     def display(self):
...         """Prints the board and metadata formatted similarly to your UI."""
...         print(f"📍 CURRENT BOARD STATE (Path Cost: {self.path_cost}):")
...         for row in self.board:
...             print(" " + " | ".join(row))
...             print("---|---|---")
...         
        counts = {'1': 0, '0': 0, ' ': 0}
        for r in self.board:
            for c in r:
                counts[c] += 1
                
        next_states = self.get_legal_next_states()
        print(f"\n📊 CURRENT STATE ANALYSIS:")
        print(f"• Current Turn: Player '{self.current_player}'")
        print(f"• Pieces Count: '1'={counts['1']}, '0'={counts['0']}")
        print(f"• Cumulative Path Cost: {self.path_cost}")
        print(f"• Branching Factor: {len(next_states)} legal next states found.")
        print("-" * 35)

        if next_states:
            print(f"🔮 LEGAL NEXT STATES FOR PLAYER '{self.current_player}':\n")
            for idx, state in enumerate(next_states, start=1):
                print(f"Option {idx} (Next Path Cost: {state.path_cost}):")
                for row in state.board:
                    print(" " + " | ".join(row))
                    print("---|---|---")
                print()


# --- Example Usage ---
if __name__ == "__main__":
    # Define initial board state matching your image:
    # 0 |   | 1
    # 1 |   |  
    # 1 | 0 | 0
    initial_board = [
        ['0', ' ', '1'],
        ['1', ' ', ' '],
        ['1', '0', '0']
    ]

    # Assume this board was reached after 6 previous moves (Path Cost = 6)
    root_node = TicTacToeNode(
        board=initial_board,
        current_player='1',
        path_cost=6
    )

    # Display current state and all calculated next states with path costs
    root_node.display()
