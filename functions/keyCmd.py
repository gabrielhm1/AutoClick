from functions.command import Command
import random
class KeyCmd(Command):


    def setKey(self,key):
        self.key = key

    def getKey(self):
        return self.key
