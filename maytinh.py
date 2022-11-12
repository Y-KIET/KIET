import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,QPushButton)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

#create class for QApplication and QMainwindow
class Pycal(QMainWindow):
    def __init__(self):
        super().__init__()
        #set title
        self.setWindowTitle("Python Calculator Tutorial")
        self.setStyleSheet("background-color: #95B9C7;")
        #set geometry
        self.setGeometry(100,100,370,350)
        
        #show widget
        self.create_widget()
       
    #create widget and buttons
    def create_widget(self):
        #create QLabel
        self.label = QLabel(self)
        self.label.setGeometry(5,5,350,80)
        self.label.setStyleSheet("QLabel{border: 4px solid brown; background: #EBF4FA; color:blue;}")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Times New Roman', 24))
        
        #create button for 1
        btn1 = QPushButton("1", self)
        btn1.setGeometry(5,150,80,40)
        btn1.setStyleSheet("background: #AAFFAA;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for 2
        btn2 = QPushButton("2", self)
        btn2.setGeometry(95,150,80,40)
        btn2.setStyleSheet("background: #AAFFAA;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for 3
        btn3 = QPushButton("3", self)
        btn3.setGeometry(185,150,80,40)
        btn3.setStyleSheet("background: #AAFFAA;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for operator (*)
        btn_mul = QPushButton("*", self)
        btn_mul.setGeometry(275,150,80,40)
        btn_mul.setStyleSheet("background: #E0FFFF;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for 4
        btn4 = QPushButton("4", self)
        btn4.setGeometry(5,200,80,40)
        btn4.setStyleSheet("background: #AAFFAA;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for 5
        btn5 = QPushButton("5", self)
        btn5.setGeometry(95,200,80,40)
        btn5.setStyleSheet("background: #AAFFAA;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for 6
        btn6 = QPushButton("6", self)
        btn6.setGeometry(185,200,80,40)
        btn6.setStyleSheet("background: #AAFFAA;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for operator (-)
        btn_minus = QPushButton("-", self)
        btn_minus.setGeometry(275,200,80,40)
        btn_minus.setStyleSheet("background: #E0FFFF;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for 7
        btn7 = QPushButton("7", self)
        btn7.setGeometry(5,250,80,40)
        btn7.setStyleSheet("background: #AAFFAA;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for 8
        btn8 = QPushButton("8", self)
        btn8.setGeometry(95,250,80,40)
        btn8.setStyleSheet("background: #AAFFAA;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for 9
        btn9 = QPushButton("9", self)
        btn9.setGeometry(185,250,80,40)
        btn9.setStyleSheet("background: #AAFFAA;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for operator (+)
        btn_plus = QPushButton("+", self)
        btn_plus.setGeometry(275,250,80,40)
        btn_plus.setStyleSheet("background: #E0FFFF;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for 0
        btn0 = QPushButton("0", self)
        btn0.setGeometry(5,300,80,40)
        btn0.setStyleSheet("background: #AAFFAA;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for point(.)
        btn_point = QPushButton(".", self)
        btn_point.setGeometry(95,300,80,40)
        btn_point.setStyleSheet("background: #AAFFAA;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for operator (/)
        btn_div = QPushButton("/", self)
        btn_div.setGeometry(185,300,80,40)
        btn_div.setStyleSheet("background: #AAFFAA;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for operator (=)
        btn_equal = QPushButton("=", self)
        btn_equal.setGeometry(275,300,80,40)
        btn_equal.setStyleSheet("background: #E0FFFF;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for open bracket
        btn_open = QPushButton("(", self)
        btn_open.setGeometry(5,100,80,40)
        btn_open.setStyleSheet("background: #AAFFAA;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for close bracket
        btn_close = QPushButton(")", self)
        btn_close.setGeometry(95,100,80,40)
        btn_close.setStyleSheet("background: #AAFFAA;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for Clear
        btn_clear = QPushButton("Clear", self)
        btn_clear.setGeometry(185,100,80,40)
        btn_clear.setStyleSheet("background: #AAFFAA;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create button for Del
        btn_del = QPushButton("Del", self)
        btn_del.setGeometry(275,100,80,40)
        btn_del.setStyleSheet("background: #E0FFFF;""font-size: 20px;" "color: blue;" "border: 2px solid brown")
        
        #create action for buttons and function
        btn1.clicked.connect(self.for1)
        btn2.clicked.connect(self.for2)
        btn3.clicked.connect(self.for3)
        btn4.clicked.connect(self.for4)
        btn5.clicked.connect(self.for5)
        btn6.clicked.connect(self.for6)
        btn7.clicked.connect(self.for7)
        btn8.clicked.connect(self.for8)
        btn9.clicked.connect(self.for9)
        btn0.clicked.connect(self.for0)
        btn_open.clicked.connect(self.for_open)
        btn_close.clicked.connect(self.for_close)
        btn_point.clicked.connect(self.for_point)
        
        btn_plus.clicked.connect(self.for_plus)
        btn_minus.clicked.connect(self.for_minus)
        btn_mul.clicked.connect(self.for_mul)
        btn_div.clicked.connect(self.for_div)
        
        btn_clear.clicked.connect(self.for_clear)
        btn_del.clicked.connect(self.for_del)
        btn_equal.clicked.connect(self.for_equal)
                
    
    #create function for buttons
    def for1(self):
        text = self.label.text()
        self.label.setText(text + "1")
        
    def for2(self):
        text = self.label.text()
        self.label.setText(text + "2")
    
    def for3(self):
        text = self.label.text()
        self.label.setText(text + "3")
        
    def for4(self):
        text = self.label.text()
        self.label.setText(text + "4")
    
    def for5(self):
        text = self.label.text()
        self.label.setText(text + "5")
        
    def for6(self):
        text = self.label.text()
        self.label.setText(text + "6")
    
    def for7(self):
        text = self.label.text()
        self.label.setText(text + "7")
        
    def for8(self):
        text = self.label.text()
        self.label.setText(text + "8")
    
    def for9(self):
        text = self.label.text()
        self.label.setText(text + "9")
        
    def for0(self):
        text = self.label.text()
        self.label.setText(text + "0")
        
    def for_point(self):
        text = self.label.text()
        self.label.setText(text + ".")
        
    def for_open(self):
        text = self.label.text()
        self.label.setText(text + "(")
    
    def for_close(self):
        text = self.label.text()
        self.label.setText(text + ")")
        
    def for_clear(self):
        self.label.setText("")
        
    def for_del(self):
        text = self.label.text()
        self.label.setText(text[:len(text)-1])
    
    def for_plus(self):
        text = self.label.text()
        self.label.setText(text + "+")
    
    def for_minus(self):
        text = self.label.text()
        self.label.setText(text + "-")
    
    def for_mul(self):
        text = self.label.text()
        self.label.setText(text + "*")
    
    def for_div(self):
        text = self.label.text()
        self.label.setText(text + "/")
    
    def for_equal(self):
        equ = self.label.text()
        try:
            ans = eval(equ)
            self.label.setText(str(ans))
        except:
            self.label.setText("Input Error")
    
        
def main():
    app = QApplication(sys.argv)
    view = Pycal()
    view.show()
    app.exec()
    app.exit()
if __name__ == '__main__':
    main()