#!/usr/bin/python3
from Const import Const


class HelloWorld:
    message = ""
    def setMessage(self, m):
        self.message = m
    def helloWorld(self):
        print(self.message)


foo = HelloWorld()
foo.setMessage(Const.messageOne)
foo.helloWorld()
foo.setMessage(Const.messageTwo)
foo.helloWorld()

bar = Const()
bar.messageOne = "Goodbye :("
print(bar.messageOne)
print(Const.messageOne)
Const.messageOne = "testing"
print(Const.messageOne)