import random

class Command:

    def __init__(self):
        pass

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setAction(self,action):
        self.action = action

    def getAction(self):
        return self.action

    def setDelay(self,delay):
        self.delay = delay

    def getDelay(self):
        return self.delay

    def getRandomDelay(self):
        splitVar = self.delay.split(" ")
        delayStart = int(splitVar[0])
        delayEnd = int(splitVar[2])
        if delayStart ==  delayEnd:
            return delayStart

        randomDelay = random.randrange(delayStart,delayEnd)
        return randomDelay

    def setRepeat(self,repeat):
        self.repeat = repeat

    def getRepeat(self):
        return self.repeat

    def getRandomRepeat(self):
        splitVar = self.repeat.split(" ")
        repeatStart = int(splitVar[0])
        repeatEnd = int(splitVar[2])
        if repeatStart == repeatEnd:
            return repeatStart

        randomRepeat = random.randrange(repeatStart,repeatEnd)
        return randomRepeat

