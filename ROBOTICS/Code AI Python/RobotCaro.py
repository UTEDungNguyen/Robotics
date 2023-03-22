import random
from tkinter import Y
import serial
import time
ArduinoUnoSerial = serial.Serial('COM8',9600) #create Serial object *REMEMBER to check the number of COM
ArduinoUnoSerial.timeout=1.5
print(ArduinoUnoSerial.readline()) #read the serial data and print it as line
print("You have new message from Arduino")

def drawBoard(board):
    #Thực hiện in ra bàn cờ
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
 
def inputPlayerLetter():
    #Cho phép người chơi nhập ký tự mà họ muốn sử dụng
    #Trả về tập hợp kiểu List với ký tự mà người chơi chọn làm phần tử đầu tiên
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
 
    if letter == 'X':
        var100=100
        ArduinoUnoSerial.write(str(var100).encode()) #send 1 to the arduino's Data code
        return ['X', 'O']
    else:
        var200=200
        ArduinoUnoSerial.write(str(var200).encode()) #send 1 to the arduino's Data code
        return ['O', 'X']
 
def whoGoesFirst():
    #Chọn ngẫu nhiên bất kỳ cho phép người chơi đi trước hay không
    if random.randint(0,1) == 0:    #0,0 la may danh truoc  1,1 la nguoi danh truoc
        return 'computer'
    else:
        return 'player'
 
def makeMove(board, letter, move):
    board[move] = letter
 
def isWinner(bo, le):
    #Trả về True nếu người chơi thắng
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))
 
def getBoardCopy(board):
    #Sao chép bàn cờ
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy
 
def isSpaceFree(board, move):
    #Trả về True nếu nước đi còn chỗ trống
    return board[move] == ' '
 
def getPlayerMove(board):
    #Lấy nước đi của người chơi
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)
 
def chooseRandomMoveFromList(board, movesList):
    #Trả về một nước đi hợp lệ
    #Trả về None nếu không còn nước đi hợp lệ
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
 
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def chooseRandomMoveFromList1(board, movesList1):
    #Trả về một nước đi hợp lệ
    #Trả về None nếu không còn nước đi hợp lệ
    possibleMoves1 = []
    for i in movesList1:
        if isSpaceFree(board, i):
            possibleMoves1.append(i)
 
    if len(possibleMoves1) != 0:
        varrandom = random.choice(possibleMoves1)
        ArduinoUnoSerial.write(str(varrandom).encode()) #send 1 to the arduino's Data code
        print(varrandom)
        return varrandom
    else:
        return None
 
def getComputerMove(board, computerLetter):
    #Xác định nước đi cho máy
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #Giải thuật cho máy chơi
    #Kiểm tra xem nước đi tiếp theo có thắng được hay không
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)  
            if isWinner(boardCopy, computerLetter):
                ArduinoUnoSerial.write(str(i).encode()) #send 1 to the arduino's Data code
                print(i)
                return i
 
    #Kiểm tra xem người chơi có thể thắng trong nước đi tiếp theo hay không
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                ArduinoUnoSerial.write(str(i).encode()) #send 1 to the arduino's Data code
                print(i)
                return i
 
    #Chọn một nước đi ở các góc bàn cờ nếu trống
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        ArduinoUnoSerial.write(str(move).encode()) #send 1 to the arduino's Data code
        print(move)
        return move
        
    #Chọn nước đi ở giữa
    if isSpaceFree(board, 5):
        ArduinoUnoSerial.write(str(5).encode()) #send 1 to the arduino's Data code
        print(5)
        return 5
 
    #Chọn một trong các nước đi ở các cạnh bên của bàn cờ
    return chooseRandomMoveFromList1(board, [2, 4, 6, 8])
 
def isBoardFull(board):
    #Trả về True nếu các nước đi không còn, ngược lại trả về False
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
 
 
print('Welcome to Tic Tac Toe!')

var = input("Enter Setpoint to consider the position of the center of the checkerboard for the robot : ").strip()
ArduinoUnoSerial.write(str(var).encode()) #send 1 to the arduino's Data code
print("You have setpoint, invite you to fight with the robot")

while True:
    #Thiết lập lại bàn cờ
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break