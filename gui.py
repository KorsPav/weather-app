import sys
from weather import Weather
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication, QMessageBox


def get_cur_temp(city):
    city_weather = Weather(city)
    cur_temp = city_weather.get_temp()
    return cur_temp


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        city = QLabel('City')

        self.city_input = QLineEdit()

        btn = QPushButton('Get current temperature')

        btn.clicked.connect(self.button_click)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(city, 1, 0)
        grid.addWidget(self.city_input, 1, 1)
        grid.addWidget(btn, 2, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Weather app')
        self.show()

    def button_click(self):
        city = self.city_input.text()
        try:
            cur_temp = get_cur_temp(city)
            self.show_cur_temp(city, cur_temp)
        except ValueError as e:
            QMessageBox.about(self, 'Error', str(e))

    def show_cur_temp(self, city, cur_temp):
        self.cur_temp_window = CurTempWindow(city, cur_temp)
        self.cur_temp_window.show()


class CurTempWindow(QWidget):
    def __init__(self, city, cur_temp):
        super().__init__()
        self.city = city
        self.cur_temp = cur_temp
        self.initUI()

    def initUI(self):
        text = f'Current temperature in {self.city} is {self.cur_temp} degrees Celsius'
        label = QLabel(text, self)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Current temperature')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w_app = MainWindow()
    sys.exit(app.exec_())
