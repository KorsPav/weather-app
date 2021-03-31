import gui
import sys
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w_app = gui.MainWindow()
    sys.exit(app.exec_())
