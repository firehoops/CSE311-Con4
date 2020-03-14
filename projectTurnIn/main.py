from tkinter import *
import tkinter.font
import tkinter.messagebox
import time
import os

root = Tk()
#Text-Based and GUI
class View:
    def __init__(self):
        self.ROW_COUNT = 6
        self.COL_COUNT = 7

    # Params: Message - takes in the user input message
    # Return: returns the userinput as a string
    def getUserInput(self, message):
        userInput = input(message)
        return userInput

    #Params: board - takes in the game board
    #Return: Returns nothing prints out the gameboard
    def displayBoard(self,board):
        printBoard = ""

        boardRotate = board[::-1]
        for r in range(self.ROW_COUNT):
            for c in range(self.COL_COUNT):
                printBoard += "|" + str(boardRotate[r][c])
            printBoard += "|\n"
        print(printBoard)

#Handle Logic
class Model:

    def __init__(self):

        self.playerValue = 1
        self.ROW_COUNT = 6
        self.COL_COUNT = 7
        self.board = [[0] * self.COL_COUNT for r in range(self.ROW_COUNT)]
        self.moveCount = 0

    #Returns the board
    def getBoard(self):
        return self.board

    #Returns true if a one of the players has 4 pieces vertically, horizontally, or diagonally.
    def winnerExists(self):

        # Check Horizontal
        for row in range(self.ROW_COUNT):
            for col in range(self.COL_COUNT - 3):
                if self.board[row][col] == self.playerValue \
                        and self.board[row][col + 1] == self.playerValue \
                        and self.board[row][col + 2] == self.playerValue \
                        and self.board[row][col + 3] == self.playerValue:
                    return True

        # Check Vertical
        for row in range(self.ROW_COUNT - 3):
            for col in range(self.COL_COUNT):
                if self.board[row][col] == self.playerValue \
                        and self.board[row + 1][col] == self.playerValue \
                        and self.board[row + 2][col] == self.playerValue \
                        and self.board[row + 3][col] == self.playerValue:
                    return True

        # Check Diagonal \
        for row in range(self.ROW_COUNT - 3):
            for col in range(self.COL_COUNT - 3):
                if self.board[row][col] == self.playerValue \
                        and self.board[row + 1][col + 1] == self.playerValue \
                        and self.board[row + 2][col + 2] == self.playerValue \
                        and self.board[row + 3][col + 3] == self.playerValue:
                    return True

        # Check Diagonal /
        for row in range(3, self.ROW_COUNT):
            for col in range(self.COL_COUNT - 3):
                if self.board[row][col] == self.playerValue \
                        and self.board[row - 1][col + 1] == self.playerValue \
                        and self.board[row - 2][col + 2] == self.playerValue \
                        and self.board[row - 3][col + 3] == self.playerValue:
                    return True


    #Checking if row is free
    #Params: Board - the game board, colChoice - users selected col , and amount of rows
    #Returns: Returns the row number if valid by checking each row in that col and seeing if there is an open space indicated by a 0
    def checkRow(self, board ,colChoice):
        for rowNum in range(self.ROW_COUNT):
            if board[rowNum][colChoice] == 0:
                return rowNum
    #Params: colChoice - user selected col
    #Returns: Checks that user inputs a valid row# then checks if the board is full, then if there is a winner, otherwise it changes player and returns True
    def makeMove(self, colChoice):

        #Makes sure the column is valid
        try:
            row = model.checkRow(model.getBoard(), colChoice)
            model.getBoard()[row][colChoice] = self.playerValue
            self.moveCount += 1

            if self.moveCount == 43:
                print("No Winner")

            if model.winnerExists():
                self.endGame()
                return False
            if self.playerValue == 1:
                self.playerValue += 1
            else:
                self.playerValue -= 1
            return True
        except:
            print("Please Enter A Valid Column \n")
            time.sleep(.5)
            return True
    #Returns: Ends the game and prints out who the winner is
    def endGame(self):
        if model.playerValue == 1:
            time.sleep(.5)
            root.destroy()
            # Label(start.root, text="Player 1 is the Winner!!", font=header).grid(row=2, column=2, rowspan=4,columnspan=6)
            print("Player 1 is the winner!!")
            return False
        else:
            time.sleep(.5)
            root.destroy()
            # Label(start.root, text="Player 2 is the Winner!!", font=header).grid(row=2, column=2, rowspan=4, columnspan=6)
            print("Player 2 is the winner!!")
            return False


# Initialize View and Model
model = Model()
view = View()

class Controller:

    #Main method
    def __init__(self):
        self.coords_col_1 = [0, 500, 100, 600]
        self.coords_col_2 = [100, 500, 200, 600]
        self.coords_col_3 = [200, 500, 300, 600]
        self.coords_col_4 = [300, 500, 400, 600]
        self.coords_col_5 = [400, 500, 500, 600]
        self.coords_col_6 = [500, 500, 600, 600]
        self.coords_col_7 = [600, 500, 700, 600]


        self.c = Canvas(root, width=700, height=600, bg="lightsky blue")
        self.buttonFrame = Frame(root, width=700, height=200)
        self.playerScoreFrame = Frame(root, width=700, height=50)
        self.bottomFrame = Frame(root, width=700, height=50)

        # Starting the game
        option = view.getUserInput("Type text or gui for your version of Connect Four\n")
        if option.lower() == "gui":
            self.gui()
        else:
            self.textView()
    # Creates the gui
    # Returns: Creates a gui by adding frames and buttons to the root window
    def gui(self):
        header = tkinter.font.Font(size=20, weight=tkinter.font.BOLD)
        Label(root, text="Connect Four", anchor=N, font=header).grid(row=0, column=2, columnspan=3)

        # Create Seperation from Board to have buttons and exit/switch view buttons

        self.c.grid(row=1, column=0, rowspan=6, columnspan=7)
        self.buttonFrame.grid(row=8, column=0, columnspan=7)
        self.playerScoreFrame.grid(row=9, column=0, columnspan=7)
        self.bottomFrame.grid(row=10, column=0, columnspan=7)
        colTracker = [*range(7)]

        Button(self.buttonFrame, text="Row 1", relief = "groove", width= 12,command=lambda: \
            self.addPiece(colTracker[0])).grid(row=8, column=0, padx = 3)
        Button(self.buttonFrame, text="Row 2", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[1])).grid(row=8, column=1, padx =3)
        Button(self.buttonFrame, text="Row 3", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[2])).grid(row=8, column=2, padx =3)
        Button(self.buttonFrame, text="Row 4", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[3])).grid(row=8, column=3, padx =3)
        Button(self.buttonFrame, text="Row 5", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[4])).grid(row=8, column=4, padx =3)
        Button(self.buttonFrame, text="Row 6", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[5])).grid(row=8, column=5, padx =3)
        Button(self.buttonFrame, text="Row 7", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[6])).grid(row=8, column=6, padx =3)


        Button(self.bottomFrame, text="Exit", relief = "groove",width=15,command=lambda: self.quit()).grid(row=10, column=2, pady = 30, padx = 15)
        Button(self.bottomFrame, text="Switch Views", relief = "groove",width= 15,command=lambda: self.switchToText()).grid(row=10,column=4)
        root.mainloop()

    #Returns: Runs the text view of the game and gets the user input and continues the game based on their choice.
    def textView(self):
        run = True
        #Game Loop
        while run:

            #User Input Loop
            while True:

                #Try/Except to make sure user gives valid input
                try:
                    view.displayBoard(model.getBoard())

                    colChoice = int(
                        view.getUserInput("Select a Column 0,1,2,3,4,5, or 6 (or type 9 to go into gui view) \n"))
                    if colChoice == 8:
                        break
                    if colChoice == 9:

                        self.gui()
                        # break
                    run = model.makeMove(colChoice)

                    break #Exits the User Input Loop
                except:
                    print("Please Enter A Valid Column \n")
                    time.sleep(.5)
        exit()

    #Adds a piece to the board
    #Params: col - user selected col
    #Returns: adds a piece to the canvas as well as adding it to the game board to track the text view and keep game logic
    def addPiece(self, col):
        #Starting coord for row 1 , x0 =5 , y0 = 500 , x1 = 105 , y1= 600
        playerValueFont = tkinter.font.Font(size=15, weight=tkinter.font.BOLD)

        if col == 0:
            if model.playerValue == 1:
                self.c.create_oval(self.coords_col_1[0], self.coords_col_1[1], self.coords_col_1[2], self.coords_col_1[3], fill="black")
                Label(root, text="Player " + str(model.playerValue+1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan = 3)
                self.coords_col_1[1] -= 100
                self.coords_col_1[3] -= 100
                model.makeMove(col)

            else:
                self.c.create_oval(self.coords_col_1[0], self.coords_col_1[1], self.coords_col_1[2], self.coords_col_1[3], fill="red")
                Label(root, text="Player " + str(model.playerValue-1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan=3)
                self.coords_col_1[1] -= 100
                self.coords_col_1[3] -= 100
                model.makeMove(col)
        if col == 1:
            if model.playerValue == 1:
                self.c.create_oval(self.coords_col_2[0], self.coords_col_2[1], self.coords_col_2[2], self.coords_col_2[3], fill="black")
                Label(root, text="Player " + str(model.playerValue+1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan = 3)
                self.coords_col_2[1] -= 100
                self.coords_col_2[3] -= 100
                model.makeMove(col)
            else:
                self.c.create_oval(self.coords_col_2[0], self.coords_col_2[1], self.coords_col_2[2], self.coords_col_2[3], fill="red")
                Label(root, text="Player " + str(model.playerValue-1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan=3)

                self.coords_col_2[1] -= 100
                self.coords_col_2[3] -= 100
                model.makeMove(col)
        if col == 2:
            if model.playerValue == 1:
                self.c.create_oval(self.coords_col_3[0], self.coords_col_3[1], self.coords_col_3[2], self.coords_col_3[3], fill="black")
                Label(root, text="Player " + str(model.playerValue+1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan = 3)
                self.coords_col_3[1] -= 100
                self.coords_col_3[3] -= 100
                model.makeMove(col)
            else:
                self.c.create_oval(self.coords_col_3[0], self.coords_col_3[1], self.coords_col_3[2], self.coords_col_3[3], fill="red")
                Label(root, text="Player " + str(model.playerValue-1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan=3)
                self.coords_col_3[1] -= 100
                self.coords_col_3[3] -= 100
                model.makeMove(col)
        if col == 3:
            if model.playerValue == 1:
                self.c.create_oval(self.coords_col_4[0], self.coords_col_4[1], self.coords_col_4[2], self.coords_col_4[3], fill="black")
                Label(root, text="Player " + str(model.playerValue+1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan = 3)
                self.coords_col_4[1] -= 100
                self.coords_col_4[3] -= 100
                model.makeMove(col)
            else:
                self.c.create_oval(self.coords_col_4[0], self.coords_col_4[1], self.coords_col_4[2], self.coords_col_4[3], fill="red")
                Label(root, text="Player " + str(model.playerValue-1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan=3)
                self.coords_col_4[1] -= 100
                self.coords_col_4[3] -= 100
                model.makeMove(col)

        if col == 4:
            if model.playerValue == 1:
                self.c.create_oval(self.coords_col_5[0], self.coords_col_5[1], self.coords_col_5[2], self.coords_col_5[3], fill="black")
                Label(root, text="Player " + str(model.playerValue+1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan = 3)
                self.coords_col_5[1] -= 100
                self.coords_col_5[3] -= 100
                model.makeMove(col)
            else:
                self.c.create_oval(self.coords_col_5[0], self.coords_col_5[1], self.coords_col_5[2], self.coords_col_5[3], fill="red")
                Label(root, text="Player " + str(model.playerValue-1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan=3)
                self.coords_col_5[1] -= 100
                self.coords_col_5[3] -= 100
                model.makeMove(col)
        if col == 5:
            if model.playerValue == 1:
                self.c.create_oval(self.coords_col_6[0], self.coords_col_6[1], self.coords_col_6[2],self.coords_col_6[3], fill="black")
                Label(root, text="Player " + str(model.playerValue+1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan = 3)
                self.coords_col_6[1] -= 100
                self.coords_col_6[3] -= 100
                model.makeMove(col)
            else:
                self.c.create_oval(self.coords_col_6[0], self.coords_col_6[1], self.coords_col_6[2],self.coords_col_6[3], fill="red")
                Label(root, text="Player " + str(model.playerValue-1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan=3)
                self.coords_col_6[1] -= 100
                self.coords_col_6[3] -= 100
                model.makeMove(col)
        if col == 6:
            if model.playerValue == 1:
                self.c.create_oval(self.coords_col_7[0], self.coords_col_7[1], self.coords_col_7[2], self.coords_col_7[3], fill="black")
                Label(root, text="Player " + str(model.playerValue+1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan = 3)
                self.coords_col_7[1] -= 100
                self.coords_col_7[3] -= 100
                model.makeMove(col)
            else:
                self.c.create_oval(self.coords_col_7[0], self.coords_col_7[1], self.coords_col_7[2], self.coords_col_7[3], fill="red")
                Label(root, text="Player " + str(model.playerValue-1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan=3)
                self.coords_col_7[1] -= 100
                self.coords_col_7[3] -= 100
                model.makeMove(col)
    #Switches the veiw from the GUI to the text view
    #Returns: Closes the GUI and runs the text view
    def switchToText(self):
        root.withdraw()
        self.textView()

    # Closes the GUI
    # Returns: destroys the root window
    def quit(self):
        root.destroy()
#Starts everything
start = Controller()
