from PyQt5.QtCore import *
import pyautogui as pg
import random
import time
class RunThread(QThread):
    def setCommand(self,allCommands):
        self.allCommands = allCommands

    def stop(self):
        self.threadActive = False
        print("Stop called")
        self.wait()

    def on_triggered():  # define your function to be executed on hot-key press
        print(text_to_print)
        x, y = pg.position()
        print(x, y)

    def clickMode(self,currentCommand):

        clickX = currentCommand.getRandomxAxis()
        clickY = currentCommand.getRandomyAxis()
        repeatTimes = currentCommand.getRandomRepeat()

        for times in range(repeatTimes):
            delay = currentCommand.getRandomDelay()
            for second in range(delay):
                time.sleep(1)
                if self.threadActive == False:
                    break

            print("CLICK",clickX ,delay, repeatTimes , sep =" ")
            pg.moveTo(clickX, clickY, duration=random.uniform(0.1, 1.2))
            pg.click(clickX, clickY)

    def keyMode(self,currentCommand):

        repeatTimes = currentCommand.getRandomRepeat()
        for times in range(repeatTimes):
            delay = currentCommand.getRandomDelay()
            for second in range(delay):
                time.sleep(1)
                if self.threadActive == False:
                    break
                print("KEY", currentCommand.getKey() , delay , repeatTimes, sep = " ")
                pg.press(currentCommand.getKey())



    def run(self):
        #ui.breakLoop.clicked.connect(stop)
        print("Thread chamada com sucesso")
        self.threadActive = True
        while self.threadActive:
            for currentCommand in self.allCommands:
                if currentCommand.getAction() == "Key":
                    self.keyMode(currentCommand)
                else:
                    self.clickMode(currentCommand)
