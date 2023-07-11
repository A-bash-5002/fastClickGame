import random
import tkinter
import timeManager
import pygame

class mainPopUp() :
    popedButtonsCount = 0
    passedButtonsCount = 0
    popUpInterval = 1000
    colors = ["red", "green", "blue", "yellow"]
    statFrameColor = "white"


class popUp(mainPopUp) :    
    def __init__(self, popUploaction, popUpWidth, popUpHeight) :

        self.popUploaction = popUploaction
        self.popUpRangeW = popUpWidth
        self.popUpRangeH = popUpHeight
        self.timeM = timeManager.gameTime()

        self.poped = False


    
    def createPopUpButton(self, mainPopUpM) :
        self.popUpX = random.randint(0, self.popUpRangeW - 20)
        self.popUpY = random.randint(0, self.popUpRangeH- 20)
        self.popUpHeight = 1
        self.popUpWidth = 2

        popUpButton = tkinter.Button(self.popUploaction, bg = random.choice(popUp.colors), command= lambda : popUp.onPress(self, mainPopUpM))
        self.popUObject = popUpButton

        self.onScreenTime = self.timeM.timePassed()

        return self.popUObject
        

    def onPress(self, mainPopUpM) :
        mainPopUpM.popedButtonsCount += 1
        mainPopUpM.statFrameColor = self.popUObject.cget("bg")

        pygame.mixer.init()
        pygame.mixer.music.load("mixkit-arcade-bonus-alert-767.wav")
        pygame.mixer.music.play()
        
        self.poped = True
        self.popUObject.destroy()
        

    def timerUpdate(self) :
        return self.timeM.timePassed()

        
