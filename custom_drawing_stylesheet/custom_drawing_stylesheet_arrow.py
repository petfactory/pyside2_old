import sys

from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui

class CollapsableArrow(QtWidgets.QFrame):

    def __init__(self, name, height, parent=None):
        super(CollapsableArrow, self).__init__(parent)

        self._arrow_color = QtGui.QColor(255, 255, 255)
        self._arrow_scale = 4.0
        self._name = name
        self._height = height
        self._arrow_expanded, self._arrow_collapsed = self.create_arrows(height)
        self.setFixedHeight(height)
        self.set_arrow_state(False)

    def get_arrow_color(self):
        return self._arrow_color

    def set_arrow_color(self, color):
        self._arrow_color = color


    def create_arrows(self, height):
        arrow_collapsed = ( QtCore.QPointF(height*.5-.5*self._arrow_scale, height*.5-1*self._arrow_scale),
                            QtCore.QPointF(height*.5+.5*self._arrow_scale, height*.5),
                            QtCore.QPointF(height*.5-.5*self._arrow_scale, height*.5+1*self._arrow_scale))

        arrow_expanded = (  QtCore.QPointF(height*.5-1*self._arrow_scale, height*.5-.5*self._arrow_scale),
                            QtCore.QPointF(height*.5+1*self._arrow_scale, height*.5-.5*self._arrow_scale),
                            QtCore.QPointF(height*.5, height*.5+.5*self._arrow_scale))

        return (arrow_expanded, arrow_collapsed)


    def paintEvent(self, e):

        qp = QtGui.QPainter(self)
        rect = QtCore.QRect(self._height, 0, self.width(), self.height())
        qp.drawText(rect, QtCore.Qt.AlignVCenter, self._name)
        qp.setBrush(self.get_arrow_color())
        qp.setPen(QtCore.Qt.NoPen)
        qp.drawPolygon(self._arrow)
        qp.end()

    def set_arrow_state(self, state):
        if state:
            self._arrow = self._arrow_expanded
        else:
            self._arrow = self._arrow_collapsed


    arrowColor = QtCore.Property(QtGui.QColor, get_arrow_color, set_arrow_color)


class TestWidget(QtWidgets.QWidget):
    
    def __init__(self, parent=None):

        super(TestWidget, self).__init__(parent)

        self.setGeometry(100,240,300,200)
        self.setWindowTitle('ui')

        vbox = QtWidgets.QVBoxLayout(self)

        arrow_1 = CollapsableArrow('Test', 20)
        vbox.addWidget(arrow_1)

        stylesheet_1 = '''
        CollapsableArrow {
            border-radius: 2px;
            color: rgb(255, 0, 0);
            background-color: rgb(100, 100, 100);
            qproperty-arrowColor: rgb(255, 0, 0);
        }'''
        arrow_1.setStyleSheet(stylesheet_1)

        arrow_2 = CollapsableArrow('Test', 20)
        arrow_2.set_arrow_state(1)
        vbox.addWidget(arrow_2)

        stylesheet_2 = '''
        CollapsableArrow {
            border-radius: 2px;
            color: rgb(0, 255, 0);
            background-color: rgb(50, 50, 50);
            qproperty-arrowColor: rgb(0, 255, 0);
        }'''

        self.setStyleSheet(stylesheet_2)
        
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = TestWidget()
    w.show()
    app.exec_()
