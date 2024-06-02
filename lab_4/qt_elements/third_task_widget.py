import matplotlib
from PyQt5.QtWidgets import QWidget, QVBoxLayout

matplotlib.use('Qt5Agg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(200)
        self.figure = Figure(figsize=(30, 5))
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.figure)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.canvas)

    def show_plot(self, x, y):
        self.axes.clear()
        self.axes.plot(x, y, linestyle='--', marker='o')
        self.axes.set_xlabel('Количество ядер')
        self.axes.set_ylabel('Секунды')
        self.axes.grid(True)
        self.axes.set_xticks(x)
        self.axes.set_xticklabels(x)

        self.canvas.draw()
        self.show()
