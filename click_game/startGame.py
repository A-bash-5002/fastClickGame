import tkinter
from main import mainFrame
import timeManager
import popUpManager

class startGame(tkinter.Tk) :
    def __init__(self) :
        super().__init__()

        self.title("Click fast")
        self.geometry("800x500")
        self.resizable(False,False)
        self.configure(bg="black")

        self.startButton = tkinter.Button(self, text="Start", font=("Arial",20), bg="yellow", command= lambda : startGame.loadGame(self))
        self.startButton.place(x = 350, y = 225, width=100, height=50)

    
    def loadGame(self) :
        timeM = timeManager.gameTime()
        mainPopUpM = popUpManager.mainPopUp()

        self.game = mainFrame(800,500,mainPopUpM,timeM)
        self.game.place(x=0,y=0)





if __name__ == "__main__" :
    newGame = startGame()

    newGame.mainloop()