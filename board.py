import random

import copy


solution_board1 = [['8','2','7','1','5','4','3','9','6'],['9','6','5','3','2','7','1','4','8'],['3','4','1','6','8','9','7','5','2'],['5','9','3','4','6','8','2','7','1'],['4','7','2','5','1','3','6','8','9'],['6','1','8','9','7','2','4','3','5'],['7','8','6','2','3','5','9','1','4'],['1','5','4','7','9','6','8','2','3'],['2','3','9','8','4','1','5','6','7']]


solution_board2 = [['5','3','4','6','7','8','9','1','2'],['6','7','2','1','9','5','3','4','8'],['1','9','8','3','4','2','5','6','7'],['8','5','9','7','6','1','4','2','3'],['4','2','6','8','5','3','7','9','1'],['7','1','3','9','2','4','8','5','6'],['9','6','1','5','3','7','2','8','4'],['2','8','7','4','1','9','6','3','5'],['3','4','5','2','8','6','1','7','9']]


solution_board3 = [['7','3','5','6','1','4','8','9','2'],['8','4','2','9','7','3','5','6','1'],['9','6','1','2','8','5','3','7','4'],['2','8','6','3','4','9','1','5','7'],['4','1','3','8','5','7','9','2','6'],['5','7','9','1','2','6','4','3','8'],['1','5','7','4','9','2','6','8','3'],['6','9','4','7','3','8','2','1','5'],['3','2','8','5','6','1','7','4','9']]


solution_board4 = [['5','4','1','2','3','8','9','7','6'],['2','3','9','6','7','1','8','5','4'],['6','7','8','4','5','9','1','2','3'],['1','2','3','5','4','6','7','8','9'],['4','5','6','8','9','7','2','3','1'],['8','9','7','1','2','3','4','6','5'],['3','1','2','7','6','4','5','9','8'],['7','6','4','9','8','5','3','1','2'],['9','8','5','3','1','2','6','4','7']]


solution_board5 = [['3','1','4','7','6','5','2','9','8'],['9','2','7','8','1','4','3','6','5'],['8','5','6','2','9','3','1','4','7'],['5','7','1','6','8','9','4','2','3'],['2','4','3','1','5','7','6','8','9'],['6','8','9','4','3','2','7','5','1'],['1','9','5','3','2','6','8','7','4'],['7','3','2','9','4','8','5','1','6'],['4','6','8','5','7','1','9','3','2']]


solution_board6 = [['3','1','4','7','6','5','2','9','8'],['9','2','7','8','1','4','3','6','5'],['8','5','6','2','9','3','1','4','7'],['5','7','1','6','8','9','4','2','3'],['2','4','3','1','5','7','6','8','9'],['6','8','9','4','3','2','7','5','1'],['1','9','5','3','2','6','8','7','4'],['7','3','2','9','4','8','5','1','6'],['4','6','8','5','7','1','9','3','2']]


solution_board7 = [['5','3','4','6','7','8','9','1','2'],['6','7','2','1','9','5','3','4','8'],['1','9','8','3','4','2','5','6','7'],['8','5','9','7','6','1','4','2','3'],['4','2','6','8','5','3','7','9','1'],['7','1','3','9','2','4','8','5','6'],['9','6','1','5','3','7','2','8','4'],['2','8','7','4','1','9','6','3','5'],['3','4','5','2','8','6','1','7','9']]


solution_board8 = [['2','1','4','7','5','6','3','9','8'],['8','7','6','9','3','1','2','4','5'],['5','3','9','8','2','4','7','6','1'],['6','4','7','2','1','5','8','3','9'],['3','9','5','6','4','8','1','2','7'],['1','8','2','3','7','9','6','5','4'],['7','6','1','4','9','3','5','8','2'],['4','2','8','5','6','7','9','1','3'],['9','5','3','1','8','2','4','7','6']]


solution_board9 = [['1','6','2','8','5','7','4','9','3'],['5','3','4','1','2','9','6','7','8'],['7','8','9','6','4','3','5','2','1'],['4','7','5','3','1','2','9','8','6'],['9','1','3','5','8','6','7','4','2'],['6','2','8','7','9','4','1','3','5'],['3','5','6','4','7','8','2','1','9'],['2','4','1','9','3','5','8','6','7'],['8','9','7','2','6','1','3','5','4']]


solution_board10 = [['8','5','6','2','1','4','7','3','9'],['1','9','3','5','7','6','8','4','2'],['2','4','7','9','8','3','1','6','5'],['4','6','2','7','5','9','3','8','1'],['9','3','1','8','6','2','4','5','7'],['7','8','5','3','4','1','9','2','6'],['6','2','4','1','9','8','5','7','3'],['3','7','9','4','2','5','6','1','8'],['5','1','8','6','3','7','2','9','4']]


def find_solution_board():
  '''
  Generates a random solution board whose problem board the player would be working on.
  Returns:
    solution_board: the solution to the problem assigned to the player.
  '''
  random_board = random.randint(1,10)
  if random_board == 1:
    solution_board = solution_board1
  elif random_board == 2:
    solution_board = solution_board2
  elif random_board == 3:
    solution_board = solution_board3
  elif random_board == 4:
    solution_board = solution_board4
  elif random_board == 5:
    solution_board = solution_board5
  elif random_board == 6:
    solution_board = solution_board6
  elif random_board == 7:
    solution_board = solution_board7
  elif random_board == 8:
    solution_board = solution_board8
  elif random_board == 9:
    solution_board = solution_board9
  else:
    solution_board = solution_board10
  return solution_board
 

def print_nice_board(lsted):
 '''
 Prints a board with a nice appearance
 Args:
   lsted: a list with a dull appearance
 '''
 star = ''
 count = 1
 
 for row in range(len(lsted)):
   
   for col in range(len(lsted[row])):
       if col == 0:
         star = star + str(count) + ' ' + '|' + ' '+ lsted[row][col] + ' '
       elif col % 3 == 2:
         star = star + ' ' + lsted[row][col] + ' ' + '|'
       else:
         star = star + ' ' + lsted[row][col] +  ' '
   count = count + 1

 ster = ''
 
 for i in range(len(star)): 
   if i % 33 == 32:
     ster = ster + star[i] + '\n'
   else:
     ster = ster + star[i]

 step = ''
 print('')
 print('    ' + '1' + '  ' + '2' + '  '+ '3' + '   '+ '4' + '  ' + '5' + '  '+ '6' + '   ' + '7' + '  ' + '8' + '  ' + '9')
 print('  _______________________________')

 for i in range(len(ster)):
   if i % 102 != 101:
     step = step + ster[i]

   else:
     step = step + ster[i] + '  _______________________________' + '\n'
  
 print(step)


def find_number_of_positions(difficulty_):
    '''
    Determines the number of positions on the solution board to have their numbers erased based on the difficulty level of the game.
    Args:
        difficulty_: the level of difficulty of the game as selected by the player.
    Returns:
        the number of positions in the solution board to have their numbers erased.    
    '''
    if difficulty_ == 'easy':
        number_of_positions = 40
    elif difficulty_ == 'medium':
        number_of_positions = 50
    elif difficulty_ == 'hard':
        number_of_positions = 55
    else:
        number_of_positions = 60
    return number_of_positions
   

def random_position(number_of_positions_):
    '''
    Determines random row and column number of the positions to have their numbers erased.
    Args:
        number_of_positions_: the total number of positions to have their numbers erased.
    Returns:
        random_row_and_col_list: a list containing the row and column number of the positions to have their numbers erased.
    '''
    random_row_and_col_num_list= [[],[]]
    
    for i in range(number_of_positions_):
      random_row_num = random.randint(0,8)
      random_col_num = random.randint(0,8)
      random_row_and_col_num_list[0].append( random_row_num)
      random_row_and_col_num_list[1].append(random_col_num)
    return random_row_and_col_num_list


def find_problem_board(board,lst):
    '''
    Erases the numbers of the selected positions to have their numbers erased.
    Args:
      board: the board containing the solution to the game.
      lst: a list containing the row numbers and column numbers of the positions.
    Returns:
        problem_board: a board that is same as the solution exept that it contains spaces to be filled by the player. 
    '''
    problem_board = copy.deepcopy(board) 
    
    for row_index in range(len(lst[0])):
        
        for col_index in range(len(lst[1])):
            if row_index == col_index:
                problem_board[lst[0][row_index]][lst[1][col_index]] = '*'
    return problem_board


def find_valid_picked_position(board_,row_number_,col_number_):
    '''
    Checks if the position a player pucked is valid and generates the coordinate of his desired position if it is valid.
    Args:
        board_: the board containing the problem.
        row_number_: the row number of the player' desired position.
        col_number_: the row number of the player' desired position.
    Returns:
        position_coordinate: a list containing the row and column number of a valid position picked by the player.
    '''
    position_coordinate = []
    
    while board_[row_number_][col_number_] != '*':
      row_number_ = int(input('That was an invalid position.Select the row number of another position you intend to insert a number: ')) 
      col_number_ = int(input('That was an invalid position.Select the column number of another position you intend to insert a number: '))
    position_coordinate.append(row_number_)
    position_coordinate.append(col_number_)
    return position_coordinate


def insert_valid_number(picked_position_,board_1,num,board_2):
  # print(problem_board)
  '''
  Checks if the player inserted by the player is correct, prompts the player to pick another number until he picks the correct answer, and, then, it updates the problem board with the correct answer.  
  Args:
    picked_position_: the valid position the player intends to insert a number.
    _board_:a board containing solution to the game.
    num = the number the player intends to insert.
    __board: the board containing the problem.
  Returns:
    __board: the board containing the problem except that an empty space has been updated to the correct number the player inserted.
  '''
  
  while board_1[picked_position_[0]][picked_position_[1]] != num:
    if int(num) < 1 or int(num) > 9:
      num = input('That number was out of range.Again, Pick a number between 1 and 9 (inclusive) to play: ')
    else:
      num = input('That was an incorrect number. Pick another number between 1 and 9(inclusive) to play: ')
  board_2[picked_position_[0]][picked_position_[1]] = num
  return board_2
