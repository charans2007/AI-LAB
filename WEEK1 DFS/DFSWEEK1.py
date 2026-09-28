Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class PuzzleState:
    def __init__(self, board, parent=None, move="", depth=0):
        self.board = board       # 2D list representing the 3x3 grid
        self.parent = parent     # Reference to parent state for path reconstruction
        self.move = move         # Move taken to reach current state
        self.depth = depth       # Tree depth level (serves as the path cost)

    def get_tuple(self):
        return tuple(tuple(row) for row in self.board)

    def is_goal(self, goal_board):
        return self.board == goal_board

    def find_blank(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    return r, c
        return None

    def get_neighbors(self):
        neighbors = []
        blank_r, blank_c = self.find_blank()
        
        # Possible movements: Row change, Column change, Label
        moves = {
            "Up": (-1, 0),
            "Down": (1, 0),
            "Left": (0, -1),
            "Right": (0, 1)
        }
        for move_name, (dr, dc) in moves.items():
            new_r, new_c = blank_r + dr, blank_c + dc
            if 0 <= new_r < 3 and 0 <= new_c < 3:
                new_board = copy.deepcopy(self.board)
                new_board[blank_r][blank_c], new_board[new_r][new_c] = new_board[new_r][new_c], new_board[blank_r][blank_c]
                neighbors.append(PuzzleState(new_board, self, move_name, self.depth + 1))
        return neighbors

def solve_dfs(start_board, goal_board, max_depth=50):
    start_state = PuzzleState(start_board)
    stack = [start_state]
    # Tracks the minimum depth at which a state configuration was visited
    visited = {}

    while stack:
        current_state = stack.pop()

        if current_state.is_goal(goal_board):
            path = []
            moves = []
            final_cost = current_state.depth
            while current_state:
                path.append(current_state.board)
                if current_state.move:
                    moves.append(current_state.move)
...                 current_state = current_state.parent
...             return path[::-1], moves[::-1], final_cost
... 
...         state_tuple = current_state.get_tuple()
...         if current_state.depth <= max_depth:
...             # Only expand if state hasn't been visited, or found at a shallower depth
...             if state_tuple not in visited or current_state.depth < visited[state_tuple]:
...                 visited[state_tuple] = current_state.depth
...                 # Reverse neighbors before pushing to preserve consistent DFS order on stack
...                 for neighbor in reversed(current_state.get_neighbors()):
...                     stack.append(neighbor)
...                     
...     return None, None, None
... 
... def print_board(board):
...     for row in board:
...         print(" ".join(str(x) if x != 0 else "_" for x in row))
...     print()
... 
... if __name__ == "__main__":
...     # --- Student Details Identification Banner ---
...     print("=" * 50)
...     print("STUDENT NAME  : CHARAN S")
...     print("REGISTER NO.  : 1WN24CS070")
...     print("ASSIGNMENT    : 8-PUZZLE GAME (DFS METHOD)")
...     print("=" * 50, "\n")
... 
...     # Your precise initial state configuration
...     initial_state = [
...         [1, 2, 3],
...         [0, 4, 6],
...         [7, 5, 8]
...     ]
... 
...     # Your precise target goal configuration
...     goal_state = [
...         [1, 2, 3],
...         [4, 5, 6],
...         [7, 8, 0]
...     ]
... 
...     print("Initial Board State Layout:")
...     print_board(initial_state)
... 
...     print("Executing DFS Solver Engine...")
...     path, moves, total_cost = solve_dfs(initial_state, goal_state, max_depth=50)
... 
...     if path is not None:
...         print("\n" + "=" * 50)
...         print(" SUCCESS: GOAL STATE REACHED!")
...         print(f" TOTAL PATH COST : {total_cost} moves")
...         print(" MOVE SEQUENCE   :", " -> ".join(moves))
...         print("=" * 50 + "\n")
...         
...         print("Detailed Step-by-Step State Transformations:")
...         for idx, step in enumerate(path):
...             print(f"Step {idx} [Current Cost cumulative: {idx}]:")
...             print_board(step)
...     else:
...         print("\nFailure: Target state unreachable within the specified maximum search depth threshold.")
