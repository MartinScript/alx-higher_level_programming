#!/usr/bin/python3

import sys


def solve_n_queens(n, board=[]):
    if n == len(board):
        return [board[:]]  # Return a copy of the solution

    solutions = []
    for col in range(n):
        board.append(col)
        if is_valid(board):
            solutions.extend(solve_n_queens(n, board))
        board.pop()
    return solutions


def is_valid(board):
    current_queen_row, current_queen_col = len(board) - 1, board[-1]
    # Check if any queens can attack each other
    for row, col in enumerate(board[:-1]):
        if col == current_queen_col or \
                col - current_queen_col == current_queen_row - row or \
                col - current_queen_col == row - current_queen_row:
            return False
    return True


def print_solution(solution):
    n = len(solution)
    for col in solution:
        print('.' * col + 'Q' + '.' * (n - col - 1))


def main():
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = solve_n_queens(n)
    for solution in solutions:
        print_solution(solution)


if __name__ == '__main__':
    main()
