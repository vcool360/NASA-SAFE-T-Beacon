#This file must be run in a directory of the entire GUI's objects such as heart rate symbol, battery icon, etc for a functional GUI to display

#This test confirms that async functionality can be implemented in the PyQt5 GUI's environment
#       async functionality achieved through QThreadPool for handling multithreading
#           and by subclassing QRunnable for signaling

#The test is proven by the async function printing indefinitely to the console
#       'proven' because its an async function operating in the GUI environment (which is natively sync-focused)


import sys
import asyncio
from asyncqt import QEventLoop

from PyQt5 import QtCore
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QTime, QThreadPool, QRunnable

#test function
async def asyncTest():
    x = 0
    while (True):
        print(f"asyncTest: {x}")
        x += 1
        await asyncio.sleep(4)


#subclassing QRunnable with  a 'worker' class
class Worker(QRunnable):
    def run(self):
        asyncio.run(asyncTest())



class HomeScreen(QGroupBox):
    def __init__(self):
        super(HomeScreen, self).__init__()
        loadUi("Home.ui", self)
        self.threadpool = QThreadPool()

        # add/update items in combo box
        self.MessagesCB.setEditable(True)
        self.MessagesCB.addItem("Async Test...")
        self.MessagesCB.setCurrentIndex(0)

        #execute test functionality
        self.runTest()

    # function for actually adjusting the text of the heart rate
    def runTest(self):
        testHandler = Worker()
        self.threadpool.start(testHandler)



app = QApplication([])
widget = QStackedWidget()
homescreen = HomeScreen()
widget.addWidget(homescreen)

# don't touch these values unless the screen being used is changed
widget.setFixedHeight(800)  # screen 400px high
widget.setFixedWidth(800)  # screen 800px wide
widget.show()

loop = QEventLoop(app)
asyncio.set_event_loop(loop)

try:
    sys.exit(app.exec())
except:
    print("Exiting")
