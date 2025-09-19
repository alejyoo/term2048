import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from board import create_board, add_random_tiles


def test_add_random_tiles_return_false():
    board = create_board(size=2)
    board[0][0] = 2
    board[0][1] = 4
    board[1][0] = 8
    board[1][1] = 16

    result = add_random_tiles(board)

    assert result is False, "should return false because the board is complete"
