from PySide2.QtGui import QPixmap ,QIcon ,QFont ,QDoubleValidator,QValidator
from PySide2.QtWidgets import QMainWindow, QApplication, QLabel ,QDesktopWidget ,QPushButton,QLineEdit
from PySide2 import QtWidgets
from sympy import *
from Equation import  Expression
import matplotlib.pyplot as plt
import sys
import time
x_values=[]
y_values=[]
class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow,self).__init__()

        self.init_ui()


    def init_ui(self):


        self.title = "Task1"
        self.setWindowTitle(self.title)
        self.setGeometry(300, 200, 250, 250)
        self.setFixedSize(750, 750)

        self.label = QtWidgets.QLabel(self)
        pixmap = QPixmap('macro.jpg')
        self.label.setPixmap(pixmap)
        self.label.setGeometry(50, -300, 1000, 800)

        self.text = QtWidgets.QLabel(self )
        self.text.setText("Enter the Equation")
        self.text.setFont(QFont('Arial', 12))
        self.text.setGeometry(70,100,200,300)

        self.equation_editor=QtWidgets.QLineEdit( self)
        self.equation_editor.setGeometry(70,280,400,35)
        self.equation_editor.setFont(QFont('Arial', 12))

        self.textMax = QtWidgets.QLabel(self )
        self.textMax.setText("Enter Max X")
        self.textMax.setFont(QFont('Arial', 12))
        self.textMax.setGeometry(70,265,140,190)

        self.equation_editorMax = QtWidgets.QLineEdit(self)
        self.equation_editorMax.setGeometry(70, 380, 120, 35)
        self.equation_editorMax.setFont(QFont('Arial', 12))


        self.textMin = QtWidgets.QLabel(self )
        self.textMin.setText("Enter Min X")
        self.textMin.setFont(QFont('Arial', 12))
        self.textMin.setGeometry(250,265,140,190)

        self.equation_editorMin = QtWidgets.QLineEdit(self)
        self.equation_editorMin.setGeometry(250, 380, 120, 35)
        self.equation_editorMin.setFont(QFont('Arial', 12))

        self.textError = QtWidgets.QLabel(self)
        self.textError.setFont(QFont('Times', 12))
        self.textError.setGeometry(480, 180, 300, 300)
        self.textError.setStyleSheet("color: red")

        self.run_button =QtWidgets.QPushButton(self)
        self.run_button.setText("run")
        self.run_button.setFont(QFont('Arial', 10))
        self.run_button.setGeometry(480,350,60,30)
        self.run_button.setStyleSheet("background-color: white")
        self.run_button.clicked.connect(self.btn_click)


        self.setIcon()
        self.center()

    def setIcon(self):
        appIcon = QIcon("macro.JPG")
        self.setWindowIcon(appIcon)

    def center(self):
        qReact = self.frameGeometry ()
        centerpoint = QDesktopWidget ().availableGeometry ().center ()
        qReact.moveCenter (centerpoint)
        self.move (qReact.topLeft ())

    def equation_check (self,string,stringmin,stringmax):
        mini =int(stringmin)
        maxi= int(stringmax)
        error =0
        if not string  :
            error =1
            return  error
        else:
            for i in string:
                if i.isalpha ():
                    if i != "x":
                        error = 1
                        return error
            x = symbols ('x ')
            fn = (Expression (string))
            for i in range (mini, (maxi + 1)):
                x_values.append (i)
                y_values.append ((fn(i)))

            return error

    def x_max_min_check(self,stringmin,stringmax):
        validation_rule = QDoubleValidator (-1000, 1000, 0)
        error = 0
        if validation_rule.validate (self.equation_editorMax.text (), 14)[0] == QValidator.State.Invalid:
            self.textError.setText (" max x parameter is invalid ")
            error =1
            return error
        if validation_rule.validate (self.equation_editorMax.text (), 14)[0] == QValidator.State.Intermediate:
            self.textError.setText (" max x parameter is invalid ")
            error =1
            return error
        if validation_rule.validate (self.equation_editorMin.text (), 14)[0] == QValidator.State.Invalid:
            self.textError.setText (" min x parameter is invalid ")
            error =1
            return error
        if validation_rule.validate (self.equation_editorMin.text (), 14)[0] == QValidator.State.Intermediate:
            self.textError.setText (" min x parameter is invalid ")
            error =1
            return error
        if int(stringmin) > int(stringmax):
            self.textError.setText ("error!min x is bigger than max x")
            error = 1
            return error
        return error

    def btn_click(self):

      equation=self.equation_editor.text()
      xmaxmiun=self.equation_editorMax.text()
      xminimum=self.equation_editorMin.text()
      x_values_check =self.x_max_min_check(xminimum,xmaxmiun)


      if x_values_check == 0:
          error_check = self.equation_check (equation, xminimum, xmaxmiun)
          if error_check != 1:

              self.textError.clear ()
              plt.plot (x_values, y_values)
              plt.xlabel ("x-axis")
              plt.ylabel ("y-axis")
              plt.title ("Equation Graph")
              plt.bar (x_values, y_values, color='r')
              plt.show ()
          else:
              self.textError.setText (" equation must be in x format ")






app = QApplication(sys.argv)
w = MyWindow()
w.show()
time.sleep(5)
w.resize(700,700)
sys.exit(app.exec_())