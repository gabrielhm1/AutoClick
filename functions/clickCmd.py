from functions.command import Command
import random
class ClickCmd(Command):

    def setxAxis(self,xAxis):
        self.xAxis = xAxis

    def getxAxis(self):
        return self.xAxis

    def getRandomxAxis(self):
        splitVar = self.xAxis.split(" ")
        x1 = int(splitVar[0])
        x2 = int(splitVar[2])
        clickX = random.uniform(x1,x2)
        return clickX


    def setyAxis(self,yAxis):
        self.yAxis = yAxis

    def getyAxis(self):
        return self.yAxis

    def getRandomyAxis(self):
        splitVar = self.yAxis.split(" ")
        y1 = int(splitVar[0])
        y2 = int(splitVar[2])
        clickY = random.uniform(y1,y2)
        return clickY