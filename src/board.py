from random import choices, sample
from typing import List, Tuple

Board = List[List[int]]
EmptyPositions = Tuple[int, int]


def create_board(size: int = 4) -> Board:
    """Create a square board depending on the size."""
    return [[0] * size for _ in range(size)]


def empty_position(board: Board) -> List[EmptyPositions]:
    """It goes through each row and column and
    returns the empty positions (row, col) in a tuple."""
    result = []
    for idx_row, row in enumerate(board):
        for idx_col, val in enumerate(row):
            if val == 0:
                result.append((idx_row, idx_col))
    return result


def add_random_tiles(board: Board, count: int = 1) -> bool:
    """Add random tiles (2 or 4) to empty board positions."""
    empty_pos = empty_position(board)

    if len(empty_pos) < count:
        return False

    selected_positions = sample(empty_pos, count)

    for row, col in selected_positions:
        tile_value = choices([2, 4], weights=[8, 2])[0]
        board[row][col] = tile_value

    return True
