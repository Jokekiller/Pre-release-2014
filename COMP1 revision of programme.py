# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

BOARDDIMENSION = 8
KashshaptuEnabled = False
from datetime import *

class score():
  def __init__(self):
    self.name = None
    self.colour = None
    self.moves = None
    self.date = None

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

def GetTypeOfGame():
    valid = False
    while not valid:
        TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
        TypeOfGame = TypeOfGame.upper()
        if TypeOfGame in ["Y", "N", "YES", "NO"]:
            valid = True
        else:
            print("Enter a value that is valid")
    return TypeOfGame

def DisplayWinner(WhoseTurn, count):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured in {0}.  White wins!".format(int(count + 1)/ 2))
    print()
    print("Well done White!")
  else:
    print("White's Sarrum has been captured in {0}.  Black wins!".format(int(count/ 2)))
    print()
    print("Well done Black")

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
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True
  elif (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) == 0):
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 2) or (abs(FinishFile - StartFile) == 2 and abs(FinishRank- StartRank) == 1):
    #All compass point directions
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckKashshaptuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckKashshaptuMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = False
  else:
    RankDifference = FinishRank - StartRank
    FileDifference = FinishFile - StartFile
    if RankDifference == 0 or FileDifference == 0:
      CheckKashshaptuMoveIsLegal = True
      #Moving like a Gisisgir
    elif abs(FinishFile - StartFile) == abs(FinishRank - StartRank):
      CheckKashshaptuMoveIsLegal = True
      #Moving like a Nabu
    elif (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 2) or (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 1):
      CheckKashshaptuMoveIsLegal = True
  return CheckKashshaptuMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
    MoveIsLegal = True
    if (FinishFile == StartFile) and (FinishRank == StartRank):
        MoveIsLegal = False
    elif StartRank in [0,BOARDDIMENSION + 1]:
        MoveIsLegal = False
    elif FinishRank in [0,BOARDDIMENSION + 1]:
        MoveIsLegal = False
    elif StartFile in [0,BOARDDIMENSION + 1]:
        MoveIsLegal = False
    elif FinishFile in [0,BOARDDIMENSION + 1]:
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
          elif PieceType == "K":
            MoveIsLegal = CheckKashshaptuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile) 
    return MoveIsLegal 

def InitialiseBoard(Board, SampleGame):
  if SampleGame == "Y":
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
            if RankNo == 1:
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
            if RankNo == 8:
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
          elif FileNo == 5:
            if RankNo == 1:
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
            if RankNo == 8:
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
    ShowOptions = False
    while not valid:
        try:
            StartSquare = int(input("Enter coordinates of square containing piece to move (file first) or enter -1 to get to the options menu: "))
            if StartSquare == -1:
              valid = True
              ShowOptions = True
            else:
              if StartSquare // 10 > 0:
                  valid = True
                  ShowOptions = False
              else:
                  print("Please enter both FILE and RANK")
        except ValueError:
            print("Please enter both FILE and RANK")
    valid = False
    while not valid and not ShowOptions:
        try:
            FinishSquare = int(input("Enter coordinates of square to move piece to (file first) or enter -1 to get to the options menu: "))
            if FinishSquare == -1:
              valid = True
              ShowOptions =  True
            else:
              if StartSquare // 10 > 0:
                  valid = True
              else:
                  print("Please enter both FILE and RANK")
        except ValueError:
            print("Please enter both FILE and RANK")
    return StartSquare, FinishSquare, ShowOptions

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  if KashshaptuEnabled and WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "WK"
    Board[StartRank][StartFile] = "  "
    print()
    print("White Redum promoted to Kashshaptu")
  elif KashshaptuEnabled and WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "BK"
    Board[StartRank][StartFile] = "  "
    print()
    print("Black Redum promoted to Kashshaptu")
  elif WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "WM"
    Board[StartRank][StartFile] = "  "
    print()
    print("White Redum promoted to Marzaz Pani")
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "BM"
    Board[StartRank][StartFile] = "  "
    print()
    print("Black Redum promoted to Marzaz Pani")
  else:
    if Board[FinishRank][FinishFile] != "  ":
        print()
        StartColour, StartName = GetPieceName(Board[StartRank][StartFile])
        FinishColour, FinishName = GetPieceName(Board[FinishRank][FinishFile])
        print("{0} {1} takes {2} {3} ".format(StartColour, StartName, FinishColour, FinishName))
        print()
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "

def ConfirmMove(StartSquare, FinishSquare):
    StartRank = StartSquare % 10
    StartFile = StartSquare // 10
    FinishRank = FinishSquare % 10
    FinishFile = FinishSquare // 10
    print()
    print("Move from File {0}, Rank {1} to File {2}, Rank {3}".format(StartFile, StartRank, FinishFile, FinishRank))
    valid = False
    while not valid:
        confirm = input("Confirm move (Yes/No): ")
        confirm = confirm.upper()[0]
        if confirm in ["Y", "N"]:
            valid = True
    if confirm == "Y":
        print("Move confirmed")
    else:
        print("Move cancelled")
        valid = False
    return valid

def GetPieceName(PieceCode):
    colour = PieceCode[0]
    piece = PieceCode[1]
    if colour == "W":
        colour = "White"
    elif colour == "B":
        colour = "Black"
    if piece == "S":
        piece = "Sarrum"
    elif piece == "M":
        piece = "Marraz Pani"
    elif piece == "N":
        piece = "Nabu"
    elif piece == "E":
        piece = "Etlu"
    elif piece == "G":
        piece = "Gisgigir"
    elif piece == "R":
        piece = "Redumn"
    elif piece == "K":
      piece = "Kashshaptu"
    return colour, piece

def DisplayMenu():
  print()
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
      choice = int(input("Please select an option: "))
      print()
      if choice in range(6):
        valid = True
      else:
        valid = False
        print("Enter a valid number")
    except ValueError:
      print("Enter a valid number")
  return choice

def MakeSelection(choice):
  if choice == 1:
    PlayGame("N", scores)
  elif choice == 2:
    pass
  elif choice == 3:
    PlayGame("Y",scores)
  elif choice == 4:
    DisplayHighScores(scores)
  elif choice == 5:
    SettingMenu()
    choice = GetSettingSelection()
    MakeSettingsSelection(choice)
  elif choice == 6:
    pass

def PlayGame(SampleGame, scores):
  Board = CreateBoard() #0th index not used
  StartSquare = 0 
  FinishSquare = 0
  ShowOptions = False
  surrender = False
  PlayAgain = "Y"
  count = 0
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
    InitialiseBoard(Board, SampleGame)
    while not(GameOver):
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal):
        StartSquare, FinishSquare, ShowOtions = GetMove(StartSquare, FinishSquare)
        GameQuit = False
        if StartSquare == -1 or FinishSquare == -1:
          ShowOptions = True
        else:
          Confirm = ConfirmMove(StartSquare, FinishSquare)
        if ShowOptions:
          OptionsMenu()
          OptionsChoice = OptionsSelection()
          surrender, GameQuit = MakeOptionsSelection(OptionsChoice, WhoseTurn)
          MoveIsLegal = True
          GameOver = True
          PlayAgain = "N"
        elif not ShowOptions:
            StartRank = StartSquare % 10
            StartFile = StartSquare // 10
            FinishRank = FinishSquare % 10
            FinishFile = FinishSquare // 10
            MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
            if not(MoveIsLegal):
              print("That is not a legal move - please try again")
            elif not GameQuit and not surrender:
              GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
              MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
              count = count + 1
              if GameOver:
                  DisplayWinner(WhoseTurn, count)
                  GetHighScore(WhoseTurn, count, scores)
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
  print("1. Save game")
  print("2. Quit to Menu")
  print("3. Return to game")
  print("4. Surrender")
  print()

def OptionsSelection():
  valid = False
  while not valid:
    try:
      OptionsChoice = int(input("Please select an option: "))
      if OptionsChoice in [1,2,3,4]:
        valid = True
      else:
        valid = False
        print("Enter a valid option")
    except ValueError:
      valid = False
      print("Enter a valid option")
  return OptionsChoice

def MakeOptionsSelection(OptionsChoice, WhoseTurn):
  surrender = False
  GameQuit = False
  if OptionsChoice == 1:
    pass
  elif OptionsChoice == 2:
    GameOver = True
    GameQuit = True
  elif OptionsChoice == 3:
    pass
  elif OptionsChoice == 4:
    surrender = True
    print()
    print("Surrendering . . .")
    print()
    if WhoseTurn == "W":
      print("White surrendered, Black wins")
    elif WhoseTurn == "B":
      print("Black surrendered, White wins")
  return surrender, GameQuit

def SettingMenu():
  print()
  print("1. Use Kashshaptu Piece")
  print("2. Return to Main Menu")
  print()

def GetSettingSelection():
  valid = False
  while not valid:
    try:
      choice = int(input("Please select an option: "))
      if choice in [1,2]:
        valid = True
      else:
        valid = False
        print("Enter a valid number")
    except ValueError:
      print("Enter a valid number")
  return choice

def MakeSettingsSelection(choice):
  GameQuit = False
  if choice == 1:
    valid = False
    while not valid:
      confirm = input("Do you want to use Kshshaptu piece?: ")
      confirm = confirm.upper()[0]
      if confirm in ["Y","N"]:
        valid = True
        if confirm == "Y":
          global KashshaptuEnabled
          KashshaptuEnabled = True
          print()
          print("Kashshaptu activated")
        else:
          global KashshaptuEnabled
          KashshaptuEnabled = False
      else:
        print("Enter a valid option")
  elif choice == 2:
    GameQuit = True
    GameOver = True

def DisplayHighScores(scores):
  print(scores)
  if scores == []:
    print("There are no high scores")
  else:
    print("High Scores")
    print()
    print("-"*46)
    print("|Name      |Colour|Number of Moves|Date      |")
    print("-"*46)
    for aScore in scores:
      print("|{0:^10}|{1:^6}|{2:^15}|{3:^10}|".format(aScore.name, aScore.colour, aScore.moves, aScore.date))
      print("-"*46)

def GetHighScore(WhoseTurn, count, scores):
  print()
  choice = input("Do you want to add your name to the high scores?: ")
  choice = choice.upper()[0]
  if choice == "Y":
    aScore = score()
    aScore.name = input("Enter your name: ")
    aScore.colour = WhoseTurn
    aScore. moves = count
    aScore.date = datetime.strftime(datetime.now(),"%d/%m/%Y")
    scores.append(aScore)
  elif choice == "N":
    aScore = None
  return aScore

if __name__ == "__main__":
  scores = []
  QuitGame = False
  while not QuitGame:
    DisplayMenu()
    choice = GetMenuSelection()
    choice = MakeSelection(choice)
    if choice == 1 or choice == 3:
      PlayGame(SampleGame, scores)
