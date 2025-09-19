from typing import List, Tuple

Board = List[List[int]]
EmptyPositions = Tuple[int, int, int]


def create_board(size: int = 4) -> Board:
    """Create a square board depending on the size."""
    return [[0] * size for _ in range(size)]


def empty_position(board: Board) -> List[EmptyPositions]:
    """It goes through each row and column and
    returns the empty positions (row, col, val) in a tuple."""
    result = []
    for idx_row, row in enumerate(board):
        for idx_col, val in enumerate(row):
            if val == 0:
                result.append((idx_row, idx_col, val))
