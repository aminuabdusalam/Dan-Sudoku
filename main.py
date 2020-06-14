from board import find_solution_board

from player import input_difficulty 

from board import find_number_of_positions 

from board import random_position

from board import find_problem_board

from board import print_nice_board 

from player import input_row_number

from player import input_col_number 

from board import find_valid_picked_position 

from player import input_desired_number

from board import insert_valid_number

def print_user_manual():
  
  '''
  shows the user manual of the game to the user
  '''
  
  print(' \t\t\t\t\t\t\t\tDAN-SUDOKU USER MANUAL\nDan-Sudoku is a puzzle game based on a 9 by 9 array of numbers. Positions on the puzzle are referred to by their row and column number. For \ninstance, the topmost left corner on the puzzle is row 1, column 1(r1c1), and the bottom right corner on the puzzle is row 9, column 9 (r9c9).\n\nThe row numbers and column numbers are shown, around the puzzle, to assist the player in identifying the different positions on the puzzle. The puzzle is subdivided into 9 sections made up of 3 by 3 arrays. For instance, section 1 is made up of r1c1,r1c2,r1c3,r2c1,r2c2,r2c3,r3c1,r3c2,\nr3c3.\n\nThe main rule governing solving Dan-Sudoku puzzles is that each row, column, and section must have only one occurence of the digits 1 through 9. In addition, a digit may not be ommitted; hence, the player is expected to fill all empty positions(denoted by asterisks) with a digit between 1 to 9 (inclusive) while ensuring that no digit appears more than once in any row, column, or section.\n\nThe puzzle gives the user prompts he/she needs to answer in order to complete the puzzle. Thus, the player needs to type the difficulty level of his/her choice(easy, medium, hard, or expert), the row and column number of the position he/she \nintends to fill, and , then, the digit he intends to fill into the empty spaces(represented by asterisks) on the puzzle. Note that the player \nneeds to press the "enter" key on the keyboard after supplying the answer to whatever question the game prompts.\n\nA Dan-Sudoku puzzle has between 20 to 50 of its position filled depending on the difficulty level selected by the player,i.e. the more the \ndifficulty level selected the more the number of positions on the puzzle that the player is expected to fill.\n\nHINT: There is one and only one solution to the Dan-Sudoku puzzle. It may be solved through logic and deduction, and no guessing is required.\nAlthough guessing might provide the right answers, players are discouraged from guessing to enable them test their brain and expose their \ncognitive abilities.\n\nAgain, to complete Dan-Sudoku puzzle, you need to deduce the placement of the digits (0-9) while ensuring that the main rule of the game is \nadhered to.')


def input_read_manual():
  '''
  Asks the user if they are done reading the manual ,and are ready to proceed to the game.
  Returns:
    read_manual: whether the player is done reading or not.
  '''
  read_manual = input('Are you done with reading the manual: ')
  read_manual = read_manual.lower()
  while read_manual == 'no':
    read_manual = input('Are you done with reading the manual: ')
    read_manual = read_manual.lower()
  return read_manual


first_timer = input('Is this your first time playing Dan-Sudoku (yes/no) : ')
first_timer = first_timer.lower()

if first_timer == 'yes':
  print('')
  print_user_manual()
  print('\n\n\n')
  input_read_manual()
else:
  print('')
  user_manual = input('Do you want to read the user manual(yes/no): ')
  user_manual = user_manual.lower()
  if user_manual == 'yes':
    print('')
    print_user_manual()
    print('\n\n\n')
    input_read_manual()
      

print('\n\n\n')


solution_board = find_solution_board()
difficulty = input_difficulty()
print('')  
number_of_positions = find_number_of_positions(difficulty) 
  
row_and_col_list = random_position(number_of_positions) 
  
problem_board = find_problem_board(solution_board,row_and_col_list)
  
print_nice_board(problem_board)


for i in range(number_of_positions - 1):
  row_number = input_row_number()
  
  col_number = input_col_number()
  
  picked_position = find_valid_picked_position(problem_board,row_number,col_number)
  
  number = input_desired_number()
  
  updated_problem_board = insert_valid_number(picked_position,solution_board,number,problem_board)

  print_nice_board(updated_problem_board)

print('You successfully completed the game.')
  




    
    
    
   

