import sys 
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()
		return

	def initUI():
		grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)


		self.setWindowTitle("Translation Assistant")
		self.move(300,300)
		self.resize(1024, 900)
		self.show()


if __nmae__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyApp()
	sys.exit(app.exec_())