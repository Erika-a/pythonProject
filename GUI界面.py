import os
import sys
import time
import shutil
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import (QWidget,QToolTip,QDesktopWidget,QMessageBox,QTextEdit,QLabel,QPushButton,QApplication,QMainWindow,QAction,qApp,QHBoxLayout,QVBoxLayout,QGridLayout,QLineEdit)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (QMainWindow,QTextEdit,
                             QAction,QFileDialog,QApplication)
from PyQt5.QtGui import QIcon


def show_w():
    '显示窗口'

    app = QApplication(sys.argv)  # 所有的PyQt5应用必须创建一个应用（Application）对象。
    # sys.argv参数是一个来自命令行的参数列表。

    w = QWidget()  # Qwidget组件是PyQt5中所有用户界面类的基础类。我们给QWidget提供了默认的构造方法。
    # 默认构造方法没有父类。没有父类的widget组件将被作为窗口使用。

    w.resize(500, 500)  # resize()方法调整了widget组件的大小。它现在是500px宽，500px高。
    w.move(500, 100)  # move()方法移动widget组件到一个位置，这个位置是屏幕上x=500,y=200的坐标。
    w.setWindowTitle('Simple')  # 设置了窗口的标题。这个标题显示在标题栏中。
    w.show()  # show()方法在屏幕上显示出widget。一个widget对象在这里第一次被在内存中创建，并且之后在屏幕上显示。

    sys.exit(app.exec_())  # 应用进入主循环。在这个地方，事件处理开始执行。主循环用于接收来自窗口触发的事件，
    # 并且转发他们到widget应用上处理。如果我们调用exit()方法或主widget组件被销毁，主循环将退出。
    # sys.exit()方法确保一个不留垃圾的退出。系统环境将会被通知应用是怎样被结束的。


def show_u():
    '显示窗口'

    app = QApplication(sys.argv)
    w = QWidget()

    w.resize(500,500)
    w.move(500,100)
    w.setWindowTitle("simple")
    w.show()

    sys.exit(app.exec())


# if __name__ == '__main__':
#     show_u()



# ##***应用图标***## #

class AppIcon(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon('t8.jpg'))
        self.show()

'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppIcon()
    sys.exit(app.exec_())
'''

# ##***提示文本***## #

class Promptext(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('sansSerif',10))
        self.setToolTip('This is a <b>QWidget</b>widget')
        btn = QPushButton('Button',self)
        btn.setToolTip('This is a </b>QPushButton</b>widget')
        btn.resize(btn.sizeHint())
        btn.move(300,100)
        self.setGeometry(300,100,600,600)
        self.setWindowTitle("Tooltips")
        self.show()
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Promptext()
    sys.exit(app.exec_())
'''
"QPushButton(string text, QWidget parent = None)"
# text参数是将显示在按钮中的内容。
# parent参数是一个用来放置我们按钮的组件。在下文例子中将会是QWidget组件。
# 一个应用的组件是分层结构的。在这个分层内，大多数组件都有父类。没有父类的组件是顶级窗口。

# 6.4 文件对话框

class FileDialog(QMainWindow):
    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        self.textedit = QTextEdit()
        self.setCentralWidget(self.textedit)
        self.statusBar()

        openfile = QAction(QIcon('t8.jpg'),'OPEN',self)
        openfile.setShortcut('Ctrl+O')
        openfile.setStatusTip('Open new file')
        openfile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openfile)

        self.setGeometry(300,300,350,300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self,'open file','/home')

        if fname[0]:
            f = open(fname[0],'r')

            with f:
                data = f.read()
                self.textedit.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileDialog()
    sys.exit(app.exec_())




