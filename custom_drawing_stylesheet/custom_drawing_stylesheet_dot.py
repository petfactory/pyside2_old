import sys
import os

from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui

class DotLabel(QtWidgets.QFrame):

    def __init__(self, name, height=20, parent=None):
        super(DotLabel, self).__init__(parent)

        self._dot_color = QtGui.QColor(0, 0, 0)
        self._name = name
        self._height = height
        self.setFixedHeight(height)

    def get_dot_color(self):
        return self._dot_color

    def set_dot_color(self, color):
        self._dot_color = color

    def paintEvent(self, e):

        qp = QtGui.QPainter(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        rect = QtCore.QRect(self._height, 0, self.width(), self._height)
        qp.drawText(rect, QtCore.Qt.AlignVCenter, self._name)
        qp.setBrush(self.get_dot_color())
        qp.setPen(QtCore.Qt.NoPen)
        qp.drawEllipse(QtCore.QPoint(self._height*.5, self._height*.5), self._height*.20, self._height*.20)
        qp.end()

    dotColor = QtCore.Property(QtGui.QColor, get_dot_color, set_dot_color)


def save_widget_png(widget, file_name):

    # make the bg transparent
    p = widget.palette()
    p.setColor(widget.backgroundRole(), QtGui.QColor(0, 0, 0, 0))
    widget.setPalette(p)

    widget.grab().save(file_name);

class TestWidget(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super(TestWidget, self).__init__(parent)

        self.setGeometry(100,240,400,200)

        vbox = QtWidgets.QVBoxLayout(self)

        # add widgets
        for i in range(3):

            dot = DotLabel('Petfactory {}'.format(i), 20+i*20)
            dot.setObjectName('dot_{}'.format(i))
            vbox.addWidget(dot)

        # apply stylesheet
        s_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'stylesheet.qss')
        with open(s_path, 'r') as f:
            self.setStyleSheet(f.read())



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = TestWidget()
    w.show()
    save_widget_png(w, "widget_screenshot.png")
    app.exec_()
