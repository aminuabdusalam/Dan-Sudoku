def input_difficulty():
  '''
 Asks the player for the difficilty level of his choice.
  Returns:
    difficulty: the level of difficulty of the game.
  '''
  difficulty = input('Select your desired difficulty level for the game (easy,medium,hard,or expert): ')
  difficulty = difficulty.lower()
  return difficulty


def input_row_number():
  '''
  Asks the player for the row number of the position he intends to insert a number.
  Returns:
    row_number: row number of the position the player intends to insert a number.
  '''
  row_number = int(input('Pick the row number of the position you intend to play: ')) - 1
  return row_number


def input_col_number(): 
  '''
  Asks the player for the column number of the position he intends to insert a number.
  Returns:
    col_number: column number of the position the player intends to insert a number.
  '''
  col_number = int(input('Pick the column number of the position you intend to play: ')) - 1
  return col_number


def input_desired_number ():
  '''
  Asks the player for the number he desires to insert in the valid position.
  Returns:
  number: the number the player desires to select into the valid position.
  '''
  number = input('Pick a number between 1 and 9 (inclusive) to play: ')
  return number 


