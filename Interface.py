import sys
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
#import Controller

class MyMainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.__initWindow()
        self.main_frame_widget = MyMainWidget(parent = self)
        self.setCentralWidget(self.main_frame_widget)

    def __initWindow(self):
        ###-------- Window layout
        self.resize(320,350)
        self.setWindowTitle('Calculator')
        ###-------- Create the menu bar
        menubar = self.menuBar()
        self.statusBar()
        menu = menubar.addMenu('Menu')
        ###-------- Options of the menu bar
        aboutAct = QAction('About', self)
        clearAct = QAction('Clear', self)
        exitAct = QAction('Exit', self)
        ###-------- Shortcuts for the menu options
        aboutAct.setShortcut('Ctrl+A')
        clearAct.setShortcut('Ctrl+C')
        exitAct.setShortcut('Ctrl+E')
        ###-------- Tip to be shown at status bar
        aboutAct.setStatusTip('Information of the program.')
        clearAct.setStatusTip('Clear everything.')
        exitAct.setStatusTip('Exit the program.')
        menu.setStatusTip('Menu button.')
        ###-------- Adding the options to the menu at menubar
        menu.addAction(aboutAct)
        menu.addAction(clearAct)
        menu.addAction(exitAct)
        ###-------- Handlers of the menu events
        aboutAct.triggered.connect(self.OnAbout)
        clearAct.triggered.connect(self.OnClear)
        exitAct.triggered.connect(self.OnExit)

    ###-------- Handlers for the menu events
    def OnAbout(self):
        QMessageBox.information(self, 'Info!', 'Simple Calculator. \n\n Author: Luis Felipe Both')

    def OnClear(self):
        ### Modify here to clear
        print('All Cleared')

    def OnExit(self):
        self.close()


class MyMainWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.__controls()
        self.__loadLayout()
        #self.__teste()

    def __controls(self):
        self.display = QLineEdit()
        ###-------- All Buttons -> 'Label':(Pos[x],Pos[y],LineSpam, CollumnSpam)
        self.buttons = {'1':(4,0,1,1),
                        '2':(4,1,1,1),
                        '3':(4,2,1,1),
                        '4':(3,0,1,1),
                        '5':(3,1,1,1),
                        '6':(3,2,1,1),
                        '7':(2,0,1,1),
                        '8':(2,1,1,1),
                        '9':(2,2,1,1),
                        '0':(5,0,1,2),
                        'AC':(1,0,1,1),
                        'C':(1,1,1,1),
                        '%':(1,2,1,1),
                        '/':(1,3,1,1),
                        '*':(2,3,1,1),
                        '-':(3,3,1,1),
                        '+':(4,3,1,1),
                        '=':(5,3,1,1),
                        ',':(5,2,1,1)}

    def __loadLayout(self):
        self.layout = QGridLayout()
        for btnText, pos in self.buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setMinimumSize(70, 50)
            self.buttons[btnText].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.buttons[btnText].setFont(QFont("Times", 15, weight=QFont.Bold))
            self.layout.addWidget(self.buttons[btnText],pos[0],pos[1],pos[2],pos[3])
        
        ###-------- Display Layout
        self.layout.addWidget(self.display,0,0,1,4)
        self.display.setFixedHeight(50)
        self.display.setContentsMargins(2,0,2,0)
        self.display.setReadOnly(True)

        ###-------- Set the hole layout
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(1,0,1,0)
        self.setLayout(self.layout)

    def __teste(self):
        for i in self.buttons.items():
            print(i[0])
