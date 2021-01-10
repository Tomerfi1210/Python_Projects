"""Nonograms, also known as Paint by Numbers, Picross, Griddlers, Pic-a-Pix, and various other names,
are picture logic puzzles in which cells in a grid must be colored or left blank according to
numbers at the side of the grid to reveal a hidden picture. In this puzzle type, the numbers are a form of discrete tomography that measures how many unbroken lines of filled-in squares there are in any given row or column. For example, a clue of "4 8 3" would mean there are sets of four,
eight, and three filled squares,
in that order, with at least one blank square between successive sets.
"""

import copy
WHITE = 0
BLACK = 1
Q_MARK = -1

def constraint_satisfactions(n, blocks):
    """
    This functions calls "_helper_constraint_satisfactions" and returns
    list of all possible options to create list with white and black according
    to a list of constraints.
    """
    result = []
    lst = [0] * n
    copy_blocks = blocks[:]
    _helper_constraint_satisfactions(n, copy_blocks, lst, 0, result)

    return result

def _helper_constraint_satisfactions(n, copy_blocks, lst, start, res):
    """
    This function returns list of all possible options to put white and black
    in a row with certain length according a list of constraints.
    """
    x = 0
    if not copy_blocks:
        tmp = []
        for i in lst:
            tmp.append(i)
        res.append(tmp)
        return

    for i in range(start, n - copy_blocks[0] + 1):
        lst[start:] = [0] * (n - start)
        for j in range(i, copy_blocks[0] + i):
            lst[j] = 1
            x = j
        _helper_constraint_satisfactions(n, copy_blocks[1:], lst, x+2, res)


def row_variations(row, blocks):
    """
    This functions returns a list of all possible options to fill in
    a row with 1 or 0 according to a list of constraints.
    """
    if not len(blocks):
        return [[WHITE] * len(row)]
    else:
        return _helper_row_variations(row, blocks, 0, [], sum(blocks))

def _helper_row_variations(row, blocks, start, lst_variations, sum_blocks):
    """
    This function works recursively. If the length of blocks equal to zero,
    the function stops and adds the row to a list of variations. The function
    returns a list of all possible variations to put white and black squares
    in a row, according to a list of constraints.
    """
    if row is None:
        return
    if not len(blocks):
        if Q_MARK in row:
            for i in range(len(row)):
                if row[i] == Q_MARK:
                    row[i] = WHITE
        lst_variations.append(row)
        return lst_variations

    if is_no_space(blocks, len(row) - start):
        # checks if there is no space left in a row
        return []

    block = blocks[0]
    rest_blocks = blocks[1:]
    if row[start] != BLACK:
        # update row with zero
        _helper_row_variations(update_row_zero(row, start), blocks, start+1,
                               lst_variations, sum_blocks)
    if row[start] != WHITE:
        # update row with block
        _helper_row_variations(row_update(row, block, start, sum_blocks),
                               rest_blocks, start + block, lst_variations,
                               sum_blocks)
    return lst_variations

def update_row_zero(row, index):
    """
    This function gets a row and creates a copy of it. If it possible,
    the function inserts zero to it in a specific index.
    """
    copy_row = row[:]
    if index <= len(row):
        copy_row[index] = WHITE
    return copy_row

def is_no_space(blocks, space):
    """
    This function checks if there is no more space in row, according to a
    number which represents the space left in a row.
    The function returns true if there is no space in a row.
    """
    if space <= 0:
        return True
    if len(blocks) > 1:
        min_square_per_blocks = sum(blocks) + len(blocks) - 1
    else:
        min_square_per_blocks = sum(blocks)
    return space < min_square_per_blocks


def row_update(row, block, start_index, sum_blocks):
    """
    This function creates a copy of a row and updates it according to a
    specific constraint.
    """
    copy_row = row[:]
    if WHITE not in row[start_index:start_index+block]:
        copy_row[start_index:start_index+block] = [BLACK]*block
        if sum_blocks < copy_row.count(BLACK):
            # check if it possible to update the row with the block
            return None
    else:
        return

    if start_index+block < len(copy_row):
        if copy_row[start_index + block] != BLACK:
            copy_row[start_index + block] = WHITE
        else:
            return None
    return copy_row

#print(row_variations([-1,-1,-1,-1,0,0],[2]))

def intersection_row(rows):
    """
    This functions gets list of rows and returns a list of
    the constraint common to all rows.
    """
    lst = []
    count = 0
    num_of_cols = rows[0]
    if not rows:
        return lst
    for i in range(len(num_of_cols)):
        for j in range(len(rows)-1):
            if rows[j][i] == rows[j+1][i]:
                count += 1
        if count == len(rows) - 1:
            # if all rows are similar in a specific index
            lst.append(rows[0][i])
        else:
            # not all rows are similar
            lst.append(Q_MARK)
        count = 0
    return lst

#print(intersection_row([[0,0,1],[0,1,1],[0,0,1]]))

def columns_from_row(board):
    """
    This function gets a board and returns a list of board's cols.
    """
    cols_as_rows = [[board[i][j] for i in range(len(board))] for j in
                    range(len(board[0]))]
    return cols_as_rows

#print(columns_from_row([[-1,0,-1],[0,-1,0]]))

def _helper_concludes(board, constraints):
    """
    This function updates the board if it possible according to draw
    conclusions from the row and columns list of constraints. If there is
    contradiction it returns none.
    """
    change = True
    while change:
        for i in range(len(board)):
            options = row_variations(board[i], constraints[0][i])
            if not options:
                # if row_variation returns none
                return None

            new_row = intersection_row(options)
            board[i] = new_row

        columns = columns_from_row(board)
        for j in range(len(columns)):
            options2 = row_variations(columns[j], constraints[1][j])
            if not options2:
                # if row_variation returns none
                return None
            new_col = intersection_row(options2)
            columns[j] = new_col

        change = False
        for row in range(len(board)):
            for col in range(len(columns)):
                if board[row][col] != columns[col][row]:
                    change = True
                    if board[row][col] != -1:
                        columns[col][row] = board[row][col]
                    if columns[col][row] != -1:
                        board[row][col] = columns[col][row]
    return board

def game_board(constraints):
    """
    This function creates a board according to a list of constraints.
    """
    board_game = []
    for j in range(len(constraints[0])):
        row = []
        for i in range(len(constraints[1])):
            row.append(Q_MARK)
        board_game.append(row)
    return board_game

def solve_easy_nonogram(constraints):
    """
    This function gets a list of constraints and returns a solved board.
    """
    board_game = game_board(constraints)
    return _helper_concludes(board_game, constraints)

print(solve_easy_nonogram([[[1],[1]],[[1],[1]]]))

def check_q_mark(board):
    """
    This function gets a board and returns true if there is no empty squares
    in it, or false if there is.
    """
    for i in range(len(board)):
        if Q_MARK in board[i]:
            return True
    return False

def update_for_board(board, color_square):
    """
    This function gets a board and color - black or white and update the
    board with one of these colors. The first index where there is an empty
    square, will be change according the color the function got.
    """
    board_copy = copy.deepcopy(board)
    for i in board_copy:
        if Q_MARK in i:
            first_q_mark = i.index(Q_MARK)
            if color_square == BLACK:
                i[first_q_mark] = BLACK
            elif color_square == WHITE:
                i[first_q_mark] = WHITE
            break
    return board_copy

def _helper_solve_nonogram(constraints, board, lst_solutions):
    """
    This function works recursively, it returns none if there is contradiction
    in solving the board or updates list of solutions with a possible
    solution which meets all list of constraints.
    """
    solution = _helper_concludes(board, constraints)

    if solution is None:
        return
    if not check_q_mark(solution):
        lst_solutions.append(solution)
        return

    update_board_black = update_for_board(board, BLACK)
    update_board_white = update_for_board(board, WHITE)

    _helper_solve_nonogram(constraints, update_board_black, lst_solutions)
    _helper_solve_nonogram(constraints, update_board_white, lst_solutions)


def solve_nonogram(constraints):
    """
    This function gets list of constraints and calls '_helper_solve_nonogram'
    to find all possible solutions of a board.
    """
    lst_solutions = []
    intermediate_solution = solve_easy_nonogram(constraints)
    if intermediate_solution is not None:
        if check_q_mark(intermediate_solution):
            _helper_solve_nonogram(constraints, intermediate_solution,
                                   lst_solutions)
        else:
            lst_solutions.append(intermediate_solution)
    return lst_solutions


print(solve_nonogram([[[1],[1],[1,1],[1],[1],[1]],[[1],[1],[1],[1],[1,1],[1]]]))