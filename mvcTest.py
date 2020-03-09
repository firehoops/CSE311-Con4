from tkinter import *
import tkinter.font
import tkinter.messagebox
import time
import os



#Text-Based and GUI
class View:
    def __init__(self):
        self.ROW_COUNT = 6
        self.COL_COUNT = 7

    #Params: board, row count, col count, user col choice, and
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
#This is where the board is created and stored during runtime.
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

    #Checking if row is free
    #Params: Board, col choice, and amount of rows
    #Returns: Returns the row number if valid
    def checkRow(self, board ,colChoice, ROW_COUNT):
        for rowNum in range(ROW_COUNT):
            if board[rowNum][colChoice] == 0:
                return rowNum
    #def addToBoard(self, board,colChoice):

    def makeMove(self, colChoice):
        row = self.checkRow(model.getBoard(), colChoice, self.ROW_COUNT)
        self.getBoard()[row][colChoice] = self.playerValue
        self.moveCount += 1

        if model.winnerExists():
            print("Winner!")
            return False

        if self.playerValue == 1:
            self.playerValue += 1
        else:
            self.playerValue -= 1
        return True



# Initialize View and Model
model = Model()
view = View()

class Controller:
    #Main method
    def __init__(self, master):
        #print(con.setBoard())
        self.coords_col_1 = [0, 500, 100, 600]
        self.coords_col_2 = [100, 500, 200, 600]
        self.coords_col_3 = [200, 500, 300, 600]
        self.coords_col_4 = [300, 500, 400, 600]
        self.coords_col_5 = [400, 500, 500, 600]
        self.coords_col_6 = [500, 500, 600, 600]
        self.coords_col_7 = [600, 500, 700, 600]
        #Starting the game
        option = self.getUserInput("Type text or gui for your version of Connect Four\n")
        if option.lower() == "gui":
            self.gui(master,c)
        else:
            self.textView(master,c)

    def textView(self,master,c):
        run = True

        #Game Loop
        while run:

            #User Input Loop
            while True:

                #Try/Except to make sure user gives valid input
                try:
                    view.displayBoard(model.getBoard())

                    colChoice = int(
                        model.getUserInput("Which Column 0,1,2,3,4,5, or 6 (or type 9 to go into gui view) \n"))
                    if colChoice == 8:
                        run = False
                        return False #Continues game
                    if colChoice == 9:
                        model.gui(master,c)

                    #self.addPiece(colChoice)
                    run = model.addPiece(colChoice)

                    break#Exits the User Input Loop
                except:
                    print("Please Enter A Valid Column \n")
                    time.sleep(.5)
        exit()

        # ***Controller?
        # Use this to get user text input
    def getUserInput(self, message):
        userInput = input(message)
        return userInput




    #Creates the gui
    #Params: master is the main root
    #Returns: Creates a gui
    def gui(self,master,c):

        header = tkinter.font.Font(size=20, weight=tkinter.font.BOLD)
        Label(master, text="Connect Four", anchor=N, font=header).grid(row=0, column=2, columnspan=2)

        # Tracking player
        player1 = True
        run = True

        # Main Canvas that board will be created and played on

        # Create Seperation from Board to have buttons and exit/switch view buttons
        bottomFrame = Frame(master, width=700, height=200)
        bottomFrame.grid(row=8, columnspan=7)
        c.grid(row=1, column=0, rowspan=6, columnspan=7)

        colTracker = [*range(7)]
        if player1:
            Button(bottomFrame, text="Row 1", command=lambda: \
                self.addPiece(c, player1, colTracker[0])).grid( row=9, column=0, sticky=E)
            Button(bottomFrame, text="Row 2", command=lambda: \
                self.addPiece(c, player1, colTracker[1])).grid(row=9, column=1, sticky=E)
            Button(bottomFrame, text="Row 3",command=lambda: \
                self.addPiece(c, player1,colTracker[2])).grid(row=9, column=2, sticky=E)
            Button(bottomFrame, text="Row 4", command=lambda: \
                self.addPiece(c, player1, colTracker[3])).grid(row=9, column=3, sticky=E)
            Button(bottomFrame, text="Row 5", command=lambda: \
                self.addPiece(c, player1, colTracker[4])).grid(row=9, column=4, sticky=E)
            Button(bottomFrame, text="Row 6", command=lambda: \
                self.addPiece(c, player1, colTracker[5])).grid(row=9, column=5, sticky=E)
            Button(bottomFrame, text="Row 7", command=lambda: \
                self.addPiece(c, player1, colTracker[6])).grid(row=9, column=6, sticky=E)

            Button(bottomFrame, text="Exit", command=lambda: self.quit(master)).grid(row=9, column=7, sticky=E)
            Button(bottomFrame, text="Switch Views", command=lambda: self.switchToText(master)).grid(row=9, column=8, sticky=E)

    #Adds a piece to the board
    #Params:Canvas, Boolean player value, col which was selected
    #Returns: Creates a piece on the board
    def addPiece(self,canvas, player1, colChoice):
        #Starting coord for row 1 , x0 =5 , y0 = 500 , x1 = 105 , y1= 600


        if colChoice == 0:
            if player1:
                canvas.create_oval(self.coords_col_1[0], self.coords_col_1[1], self.coords_col_1[2], self.coords_col_1[3], fill="black")

                self.coords_col_1[1] -= 100
                self.coords_col_1[3] -= 100
                model.makeMove(colChoice)


            else:
                canvas.create_oval(self.coords_col_1[0], self.coords_col_1[1], self.coords_col_1[2], self.coords_col_1[3], fill="red")
        if colChoice == 1:
            if player1:
                canvas.create_oval(self.coords_col_2[0], self.coords_col_2[1], self.coords_col_2[2], self.coords_col_2[3], fill="black")
                # self.coords_col_1[0] -= 100
                self.coords_col_2[1] -= 100
                # self.coords_col_1[2] -= 100
                self.coords_col_2[3] -= 100
                model.makeMove(colChoice)
            else:
                canvas.create_oval(self.coords_col_2[0], self.coords_col_2[1], self.coords_col_2[2], self.coords_col_2[3], fill="red")
        if colChoice == 2:
            if player1:
                canvas.create_oval(self.coords_col_3[0], self.coords_col_3[1], self.coords_col_3[2], self.coords_col_3[3], fill="black")
                # self.coords_col_1[0] -= 100
                self.coords_col_3[1] -= 100
                # self.coords_col_1[2] -= 100
                self.coords_col_3[3] -= 100
                model.makeMove(colChoice)
            else:
                canvas.create_oval(self.coords_col_3[0], self.coords_col_3[1], self.coords_col_3[2], self.coords_col_3[3], fill="red")
        if colChoice == 3:
            if player1:
                canvas.create_oval(self.coords_col_4[0], self.coords_col_4[1], self.coords_col_4[2], self.coords_col_4[3], fill="black")
                # self.coords_col_1[0] -= 100
                self.coords_col_4[1] -= 100
                # self.coords_col_1[2] -= 100
                self.coords_col_4[3] -= 100
                model.makeMove(colChoice)
            else:
                canvas.create_oval(self.coords_col_4[0], self.coords_col_4[1], self.coords_col_4[2], self.coords_col_4[3], fill="red")
        if colChoice == 4:
            if player1:
                canvas.create_oval(self.coords_col_5[0], self.coords_col_5[1], self.coords_col_5[2], self.coords_col_5[3], fill="black")
                # self.coords_col_1[0] -= 100
                self.coords_col_5[1] -= 100
                # self.coords_col_1[2] -= 100
                self.coords_col_5[3] -= 100
                model.makeMove(colChoice)
            else:
                canvas.create_oval(self.coords_col_5[0], self.coords_col_5[1], self.coords_col_5[2], self.coords_col_5[3], fill="red")
        if colChoice == 5:
            if player1:
                canvas.create_oval(self.coords_col_6[0], self.coords_col_6[1], self.coords_col_6[2],
                                   self.coords_col_6[3], fill="black")
                # self.coords_col_1[0] -= 100
                self.coords_col_6[1] -= 100
                # self.coords_col_1[2] -= 100
                self.coords_col_6[3] -= 100
                model.makeMove(colChoice)
            else:
                canvas.create_oval(self.coords_col_6[0], self.coords_col_6[1], self.coords_col_6[2],
                                   self.coords_col_6[3], fill="red")
        if colChoice == 6:
            if player1:
                canvas.create_oval(self.coords_col_7[0], self.coords_col_7[1], self.coords_col_7[2], self.coords_col_7[3], fill="black")
                # self.coords_col_1[0] -= 100
                self.coords_col_7[1] -= 100
                # self.coords_col_1[2] -= 100
                self.coords_col_7[3] -= 100
                model.makeMove(colChoice)
            else:
                canvas.create_oval(self.coords_col_7[0], self.coords_col_7[1], self.coords_col_7[2], self.coords_col_7[3], fill="red")

    #Switches the veiw from the GUI to the text view
    #Params: Master represents the root
    #Returns: Closes the GUI and runs the text view
    def switchToText(self,master):
        master.destroy()
        self.textView(master)

    # Closes the GUI
    # Params: Master represents the root
    # Returns: Nothing
    def quit(self,master):
        master.quit()
    #Runs the text view
    #Params: None
    #Returns: Creates the text view board

#Starts Tkinter window and runs in loop until user exits
root = Tk()
start = Controller(root)
root.mainloop()
c = Canvas(root, width=700, height=600, bg="gray")