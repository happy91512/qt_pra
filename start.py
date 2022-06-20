from multiprocessing.connection import wait
from PyQt5 import QtWidgets, QtGui, QtCore
from control import MainWindow


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())