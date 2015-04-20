# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

import pickle
BOARDDIMENSION = 8

def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")

def DisplayMenu():
    print("Main Menu")
    print()
    print("1. Start new game")
    print("2. Load existing game")
    print("3. Play sample game")
    print("4. View high scores")
    print("5. Settings")
    print("6. Quit program")
    print()

def GetMenuSelection():
    valid = False
    while not valid:
      try:
        Choice = int(input("Select an option from the menu: "))
        print()
        if not Choice in range(6):
          valid = False
          print("Enter a valid number")
        else:
          valid = True
      except ValueError:
        print("Enter a valid number")
    return Choice

def MakeSelection(Choice):
    if Choice == 1:
      PlayGame('N')
    elif Choice == 2:
      pass
    elif Choice == 3:
      PlayGame('Y')
    elif Choice == 4:
      pass
    elif Choice == 5:
      pass
    elif Choice == 6:
      pass

def PlayGame(SampleGame):
  Board = CreateBoard() #0th index not used
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  ShowOptions = False
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
    #SampleGame = GetTypeOfGame()
    InitialiseBoard(Board, SampleGame)
    while not(GameOver):
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal):
        StartSquare, FinishSquare, ShowOptions = GetMove(StartSquare, FinishSquare)
        if ShowOptions:
          OptionsMenu()
          OptionsChoice = OptionsSelection()
          MakeOptionSelection(OptionsChoice, WhoseTurn)
          #Look at notes and refactor bottom part of the Gameover thing if game quit is = to no or yes
        confirm = ConfirmMove(StartSquare, FinishSquare)
        if confirm == "No" or confirm == "N" or confirm == "no" or confirm == "n":
          StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare)
        StartRank = StartSquare % 10
        StartFile = StartSquare // 10
        FinishRank = FinishSquare % 10
        FinishFile = FinishSquare // 10
        MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
        if not(MoveIsLegal):
          print("That is not a legal move - please try again")
      GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
      MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
      if GameOver:
        DisplayWinner(WhoseTurn)
      if WhoseTurn == "W":
        WhoseTurn = "B"
      else:
        WhoseTurn = "W"
    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
      PlayAgain = chr(ord(PlayAgain) - 32)
      
def OptionsMenu():
    print()
    print("Options")
    print()
    print("1. Save Game")
    print("2. Quit to Menu")
    print("3. Return to Game")
    print("4. Surrender")
    print()
    
def OptionsSelection():
    valid = False
    while not valid:
      OptionChoice = int(input("Please select an option: "))
      if not OptionChoice in [1,2,3,4]:
        valid = False
      else:
        valid = True
    return OptionChoice

def MakeOptionSelection(OptionChoice, WhoseTurn):
  surrender = False
  GameQuit = False
  if OptionChoice == 1:
     pass
     #with open("SarrumGame.dat", mode= "rb") as binary_file:
     # pickle.dump(Board, binary_file)
  elif OptionChoice == 2:
    Gameover = True
    GameQuit = True
  elif OptionChoice == 3:
    pass
  elif OptionChoice == 4:
    surrender = True
    print()
    print("Surrendering...")
    print()
    if WhoseTurn == "W":
      print("White surrendered, Black Wins!")
    elif WhoseTurn == "B":
      print("Black surrendered, White Wins!")
  return surrender, GameQuit
  
    
def GetTypeOfGame():
    valid = False
    while not valid:
        TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
        if (TypeOfGame == 'Y') or (TypeOfGame == 'y') or (TypeOfGame == 'yes') or (TypeOfGame == 'Yes') or (TypeOfGame == 'N') or (TypeOfGame == 'n') or (TypeOfGame == 'No') or (TypeOfGame == 'no'):
            valid = True
        else:
            print("Enter a valid choice (y or n)")
    return TypeOfGame

def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("     -------------------------")
    print("R{0}".format(RankNo), end="   ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("     -------------------------")
  print()
  print("      F1 F2 F3 F4 F5 F6 F7 F8")
  print()
  print()    

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if FinishRank == StartRank - 1 or (StartRank == 7 and FinishRank == StartRank - 2):
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1 or (StartRank == 2 and FinishRank == StartRank + 2):
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  if abs(FinishFile - StartFile) == abs(FinishRank - StartRank):
    CheckNabuMoveIsLegal = True
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1) or (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1):
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 1) or (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  if (FinishFile == StartFile) and (FinishRank == StartRank):
    MoveIsLegal = False
  elif StartRank > BOARDDIMENSION or FinishRank > BOARDDIMENSION or StartFile > BOARDDIMENSION or FinishFile > BOARDDIMENSION:
      MoveIsLegal = False
  else:
    PieceType = Board[StartRank][StartFile][1]
    PieceColour = Board[StartRank][StartFile][0]
    if WhoseTurn == "W":
      if PieceColour != "W":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "W":
        MoveIsLegal = False
    else:
      if PieceColour != "B":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "B":
        MoveIsLegal = False
    if MoveIsLegal == True:
      if PieceType == "R":
        MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
      elif PieceType == "S":
        MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "M":
        MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "G":
        MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "N":
        MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "E":
        MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  return MoveIsLegal

def InitialiseBoard(Board, SampleGame):
  if SampleGame == 'Y':
    InitialiseSampleBoard(Board)
  else:
    InitialiseNewBoard(Board)

def InitialiseNewBoard(Board):
  for RankNo in range(1, BOARDDIMENSION + 1):
    for FileNo in range(1, BOARDDIMENSION + 1):
      if RankNo == 2:
        Board[RankNo][FileNo] = "BR"
      elif RankNo == 7:
        Board[RankNo][FileNo] = "WR"
      elif RankNo == 1 or RankNo == 8:
        if RankNo == 1:
          Board[RankNo][FileNo] = "B"
        if RankNo == 8:
          Board[RankNo][FileNo] = "W"
        if FileNo == 1 or FileNo == 8:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
        elif FileNo == 2 or FileNo == 7:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
        elif FileNo == 3 or FileNo == 6:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
        elif FileNo == 4:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
        elif FileNo == 5:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
      else:
        Board[RankNo][FileNo] = "  "

def InitialiseSampleBoard(Board):
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        Board[RankNo][FileNo] = "  "
    Board[1][2] = "BG"
    Board[1][4] = "BS"
    Board[1][8] = "WG"
    Board[2][1] = "WR"
    Board[3][1] = "WS"
    Board[3][2] = "BE"
    Board[3][8] = "BE"
    Board[6][8] = "BR"

def GetMove(StartSquare, FinishSquare):
  valid = False
  showOptions = False
  while not valid:
      StartSquare = input("Enter coordinates of square containing piece to move (file first)or type '-1'for menu: ")
      if StartSquare == '-1':
        valid = True
        showOptions = True
      else:
        if len(StartSquare) == 2:
            if ord(StartSquare[0]) >= 49 and ord(StartSquare[0]) <= 57 and ord(StartSquare[1]) >= 49 and ord(StartSquare[1]) <= 57 :
                StartSquare = int(StartSquare)
                valid = True
        else:
            valid = False
            print("Please provide both FILE and RANK for this move")
  correct = False
  while not correct and not showOptions:
    FinishSquare = input("Enter coordinates of square to move piece to (file first): ")
    if len(FinishSquare) == 2:
      if ord(FinishSquare[0]) >= 49 and ord(FinishSquare[0]) <= 57 and ord(FinishSquare[1]) >= 49 and ord(FinishSquare[1]) <= 57 :
        FinishSquare = int(FinishSquare)
        correct = True
      else:
        correct = False
        print("Please provide both FILE and RANK for this move")
  return StartSquare, FinishSquare, showOptions

def ConfirmMove(StartSquare, FinishSquare):
  StartSquare = str(StartSquare)
  FinishSquare = str(FinishSquare)
  print("Move from rank {0}, File {1} to Rank {2}, File {3}".format(StartSquare[0], StartSquare[1], FinishSquare[0], FinishSquare[1]))
  confirm = input("Confirm move (Yes/No): ")
  return confirm

def GetPieceName(piece):
  colour = "White"
  if piece[0] == "B":
    colour = "Black"
  name = ''
  if piece[1] == "S":
    name = "Sarrum"
  elif piece[1] == "M":
    name = "Marraz Pani"
  elif piece[1] == "N":
    name = "Nabu"
  elif piece[1] == "E":
    name = "Etiu"
  elif piece[1] == "G":
    name = "Gisgigir"
  else:
    name = "Redum"
  return colour, name

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "WM"
    Board[StartRank][StartFile] = "  "
    print("White Redum promoted to Marraz Pani")
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "BM"
    Board[StartRank][StartFile] = "  "
    print("Black Redum promoted to Marraz Pani")
  else:
    if Board[FinishRank][FinishFile] != "  ":
      FinishColour, FinishName = GetPieceName(Board[FinishRank][FinishFile])
      StartColour, StartName = GetPieceName(Board[StartRank][StartFile])
      print("{0} {1} takes {2} {3} ".format(StartColour, StartName, FinishColour, FinishName))
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "
    
if __name__ == "__main__":
  QuitGame = False
  while not QuitGame:
    DisplayMenu()
    Choice = GetMenuSelection()
    Choice = MakeSelection(Choice)
    if Choice == 1 or Choice == 3:
      PlayGame(SampleGame)
  
