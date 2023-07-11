import tkinter
import popUpManager
import pygame

class gameFrame(tkinter.Frame) :
    
    def __init__(self,width, height,mainPopUpM):
        super().__init__(width=width,height=height)
        self.configure(bg = "black")
        self.mainPopUpM = mainPopUpM

        
        gameFrame.addButton(self, width, height)



    def addButton(self, width, height) :  
        popUp = popUpManager.popUp(self,width,height)

        self.button = popUp.createPopUpButton(self.mainPopUpM)
        self.button.place(x = popUp.popUpX, y = popUp.popUpY, width=popUp.popUpWidth, height=popUp.popUpHeight)

        gameFrame.update(self, popUp)

        if self.mainPopUpM.popUpInterval > 750 :
            self.mainPopUpM.popUpInterval = self.mainPopUpM.popUpInterval - 50
        
        self.after(self.mainPopUpM.popUpInterval, lambda : gameFrame.addButton(self, width, height))


    def update(self, popUp) :
        timePassed = popUp.timerUpdate()

        if not popUp.poped :

            if timePassed > 8 :
                self.mainPopUpM.passedButtonsCount += 1
                self.mainPopUpM.statFrameColor = popUp.popUObject.cget("bg")
                
                pygame.mixer.init()
                pygame.mixer.music.load("mixkit-losing-bleeps-2026.wav")
                pygame.mixer.music.play()

                popUp.popUObject.destroy()
                del popUp

            elif timePassed < 4 :
                popUp.popUpWidth = popUp.popUpWidth + 1
                popUp.popUpHeight = popUp.popUpHeight + 1

                popUp.popUObject.place(x = popUp.popUpX, y = popUp.popUpY, width=popUp.popUpWidth, height=popUp.popUpHeight)
                self.after(100, lambda : gameFrame.update(self, popUp))

            else :
                popUp.popUpWidth = popUp.popUpWidth - 1
                popUp.popUpHeight = popUp.popUpHeight - 1

                popUp.popUObject.place(x = popUp.popUpX, y = popUp.popUpY, width=popUp.popUpWidth, height=popUp.popUpHeight)
                self.after(100, lambda : gameFrame.update(self, popUp))
        else :
            del popUp




class statFrame(tkinter.Frame) :
    def __init__(self,width, height, mainPopUpM, timeM) :
        super().__init__(width = width, height = height)
        self.timeM = timeM
        self.mainPopUpM = mainPopUpM
        
        self.commonColor = mainPopUpM.statFrameColor

        self.configure(bg=self.commonColor)

        self.counterLabel = tkinter.Label(self,text="Clicked : ",font=("Arial",20,"bold"), bg=self.commonColor)
        self.counterLabel.place(x=25,y=25,height=50)

        self.counterAmountLabel = tkinter.Label(self,text="0",font=("Arial",20,"bold"), bg=self.commonColor)
        self.counterAmountLabel.place(x=150,y=25,height=50)


        self.timeLabel = tkinter.Label(self,text="Time : ",font=("Arial",20,"bold"), bg=self.commonColor)
        self.timeLabel.place(x=200,y=25,height=50)
        
        self.time = tkinter.Label(self,text="0.0",font=("Arial",20), bg=self.commonColor)
        self.time.place(x=300,y=25,height=50)


        self.passedLabel = tkinter.Label(self,text="Passed : ",font=("Arial",20,"bold"), bg=self.commonColor)
        self.passedLabel.place(x=400,y=25,height=50)

        self.passedAmountLabel = tkinter.Label(self,text="0",font=("Arial",20,"bold"), bg=self.commonColor)
        self.passedAmountLabel.place(x=550,y=25,height=50)


        statFrame.update(self)

    
    def update(self) :
        self.time["text"] = self.timeM.timePassed()
        self.counterAmountLabel.configure(text=self.mainPopUpM.popedButtonsCount)
        self.passedAmountLabel.configure(text=self.mainPopUpM.passedButtonsCount)
        statFrame.colorUpdate(self)
        
        self.after(10,lambda : statFrame.update(self))


    def colorUpdate(self) :
        self.commonColor = self.mainPopUpM.statFrameColor

        self.configure(bg=self.commonColor)
        self.counterLabel.configure(bg=self.commonColor)
        self.counterAmountLabel.configure(bg=self.commonColor)
        self.timeLabel.configure(bg=self.commonColor)
        self.time.configure(bg=self.commonColor)
        self.passedLabel.configure(bg=self.commonColor)
        self.passedAmountLabel.configure(bg=self.commonColor)







class mainFrame(tkinter.Frame) :

    def __init__(self, width, height, mainPopUpM, timeM):
        super().__init__(width=width, height=height)

        self.gameFrame = gameFrame(width=800,height=400, mainPopUpM=mainPopUpM)
        self.gameFrame.place(x = 0,y = 100)

        self.statFrame = statFrame(width=800, height=100, mainPopUpM=mainPopUpM, timeM = timeM)
        self.statFrame.place(x = 0, y = 0)




        
