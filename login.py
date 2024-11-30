import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        email=self.email.text()
        password=self.password.text()
        self.LoginButton.clicked.connect(self.loginFunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createButton.clicked.connect(self.gotoCreate)
    def loginFunction(self):
        email=self.email.text()
        password=self.password.text()
        print("Başarılı giriş yapıldı email:",email,"şifre:",password)
    def gotoCreate(self):
        created = Creat()
        widget.addWidget(created)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Creat(QDialog):
    def __init__(self):
        super(Creat,self).__init__()
        loadUi("sign_up.ui", self)
        self.signButton.clicked.connect(self.signFunction)
    def signFunction(self):
        password=self.password.text()
        if self.password.text()==self.confirm.text():
            email = self.email.text()
            print("Başarılı bir şekilde hesabınız oluşturuldu, email:",email,"şifre:",password)
        else:
            print("Şifreler aynı değil")


app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(490)
widget.setFixedHeight(620)
widget.show()
app.exec_()