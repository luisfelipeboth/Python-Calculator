import sys
from PyQt5.QtWidgets import *
from Interface import MyMainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyMainWindow()
    myapp.show()
    sys.exit(app.exec_())