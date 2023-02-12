from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(316, 183)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblLogin = QtWidgets.QLabel(self.centralwidget)
        self.lblLogin.setGeometry(QtCore.QRect(50, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblLogin.setFont(font)
        self.lblLogin.setObjectName("lblLogin")
        self.lblPassword = QtWidgets.QLabel(self.centralwidget)
        self.lblPassword.setGeometry(QtCore.QRect(20, 60, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblPassword.setFont(font)
        self.lblPassword.setObjectName("lblPassword")
        self.leLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.leLogin.setGeometry(QtCore.QRect(110, 20, 191, 20))
        self.leLogin.setObjectName("leLogin")
        self.lePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lePassword.setGeometry(QtCore.QRect(110, 70, 191, 20))
        self.lePassword.setObjectName("lePassword")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(20, 110, 281, 23))
        self.btnLogin.setObjectName("btnLogin")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 316, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addFunctions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblLogin.setText(_translate("MainWindow", "Login:"))
        self.lblPassword.setText(_translate("MainWindow", "Password:"))
        self.btnLogin.setText(_translate("MainWindow", "Login / Register"))

    def addFunctions(self):
        self.btnLogin.clicked.connect(lambda: self.checkAccount(self.leLogin.text(), self.lePassword.text()))

    def RSAEncode(self, text: str):
        return rsa.encrypt(e, N, text)

    def checkDataForSpecialCharacters(self, username, password):
        if (':' in username) or (':' in password):
            print("Error! Expected ':'.")
            return True;
        if (username == "") or (password == ""):
            print("Error! Value(s) is empty!")
            return True;

    def checkAccount(self, username: str, password: str):
        if self.checkDataForSpecialCharacters(username, password) is True:
            return False
        rsaLine = str(self.RSAEncode(username)) + ":" + str(self.RSAEncode(password))
        with open('users.txt', 'r+') as file:
            if rsaLine in file.read():
                print("The user is logged in.")
                self.Login()
            else:
                file.write(rsaLine + '\n')
                print("The user is registered.")
                print("The user is logged in.")
                self.Login()

    def Login(self):
        MainWindow.close()
        FormPersonalAccount.show()

class Ui_FormPersonalAccount(object):
    def setupUi(self, FormPersonalAccount):
        FormPersonalAccount.setObjectName("FormPersonalAccount")
        FormPersonalAccount.resize(875, 437)
        self.centralwidget = QtWidgets.QWidget(FormPersonalAccount)
        self.centralwidget.setObjectName("centralwidget")
        self.teTextToEncode = QtWidgets.QTextEdit(self.centralwidget)
        self.teTextToEncode.setGeometry(QtCore.QRect(10, 30, 281, 281))
        self.teTextToEncode.setObjectName("teTextToEncode")
        self.lblEncode = QtWidgets.QLabel(self.centralwidget)
        self.lblEncode.setGeometry(QtCore.QRect(10, 0, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblEncode.setFont(font)
        self.lblEncode.setObjectName("lblEncode")
        self.lblDecode = QtWidgets.QLabel(self.centralwidget)
        self.lblDecode.setGeometry(QtCore.QRect(300, 0, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblDecode.setFont(font)
        self.lblDecode.setObjectName("lblDecode")
        self.teTextFromFileWithDecode = QtWidgets.QTextEdit(self.centralwidget)
        self.teTextFromFileWithDecode.setGeometry(QtCore.QRect(300, 30, 281, 281))
        self.teTextFromFileWithDecode.setObjectName("teTextFromFileWithDecode")
        self.leFilePath = QtWidgets.QLineEdit(self.centralwidget)
        self.leFilePath.setGeometry(QtCore.QRect(90, 320, 491, 20))
        self.leFilePath.setObjectName("leFilePath")
        self.lblFilePath = QtWidgets.QLabel(self.centralwidget)
        self.lblFilePath.setGeometry(QtCore.QRect(10, 320, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblFilePath.setFont(font)
        self.lblFilePath.setObjectName("lblFilePath")
        self.btnEncode = QtWidgets.QPushButton(self.centralwidget)
        self.btnEncode.setGeometry(QtCore.QRect(620, 30, 231, 51))
        self.btnEncode.setObjectName("btnEncode")
        self.btnGetTextFromFileWithDecode = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetTextFromFileWithDecode.setGeometry(QtCore.QRect(620, 90, 231, 51))
        self.btnGetTextFromFileWithDecode.setObjectName("btnGetTextFromFileWithDecode")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(620, 150, 231, 51))
        self.btnExit.setObjectName("btnExit")
        FormPersonalAccount.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FormPersonalAccount)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 875, 21))
        self.menubar.setObjectName("menubar")
        FormPersonalAccount.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FormPersonalAccount)
        self.statusbar.setObjectName("statusbar")
        FormPersonalAccount.setStatusBar(self.statusbar)

        self.retranslateUi(FormPersonalAccount)
        QtCore.QMetaObject.connectSlotsByName(FormPersonalAccount)

        self.addFunctions()

    def retranslateUi(self, FormPersonalAccount):
        _translate = QtCore.QCoreApplication.translate
        FormPersonalAccount.setWindowTitle(_translate("FormPersonalAccount", "FormPersonalAccount"))
        self.lblEncode.setText(_translate("FormPersonalAccount", "Encode"))
        self.lblDecode.setText(_translate("FormPersonalAccount", "Decode"))
        self.lblFilePath.setText(_translate("FormPersonalAccount", "FilePath:"))
        self.btnEncode.setText(_translate("FormPersonalAccount", "Encode"))
        self.btnGetTextFromFileWithDecode.setText(_translate("FormPersonalAccount", "Get text with decode"))
        self.btnExit.setText(_translate("FormPersonalAccount", "Exit"))

    def addFunctions(self):
        self.btnExit.clicked.connect(lambda: self.Exit())
        self.btnEncode.clicked.connect(lambda: self.writeToEncodedFile(self.teTextToEncode.toPlainText(), self.leFilePath.text()))
        self.btnGetTextFromFileWithDecode.clicked.connect(lambda: self.getTextFromEncodedFile(self.leFilePath.text()))

    def Exit(self):
        FormPersonalAccount.close()
        FormExit.show()

    def RSAEncode(self, text: str):
        return rsa.encrypt(e, N, text)

    def RSADecode(self, text: int):
        return rsa.decrypt(e, N, text)
    
    def writeToEncodedFile(self, text: str, filePath: str):
        with open(filePath, 'w') as file:
            file.write(self.RSAEncode(text))
        file.close()

    def getTextFromEncodedFile(self, filePath: str):
        self.teTextFromFileWithDecode.setText("")
        import os.path
        if os.path.exists(filePath):
            with open(filePath, 'r') as file:
                for line in file:
                    self.teTextFromFileWithDecode.setText(self.teTextFromFileWithDecode.toPlainText() + self.RSADecode(line))

class Ui_FormExit(object):
    def setupUi(self, FormExit):
        FormExit.setObjectName("FormExit")
        FormExit.resize(316, 184)
        self.centralwidget = QtWidgets.QWidget(FormExit)
        self.centralwidget.setObjectName("centralwidget")
        self.lblExit = QtWidgets.QLabel(self.centralwidget)
        self.lblExit.setGeometry(QtCore.QRect(70, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblExit.setFont(font)
        self.lblExit.setObjectName("lblExit")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(50, 70, 75, 23))
        self.btnExit.setObjectName("btnExit")
        self.btnGoMainWindow = QtWidgets.QPushButton(self.centralwidget)
        self.btnGoMainWindow.setGeometry(QtCore.QRect(160, 70, 91, 23))
        self.btnGoMainWindow.setObjectName("btnGoMainWindow")
        FormExit.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FormExit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 316, 21))
        self.menubar.setObjectName("menubar")
        FormExit.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FormExit)
        self.statusbar.setObjectName("statusbar")
        FormExit.setStatusBar(self.statusbar)

        self.retranslateUi(FormExit)
        QtCore.QMetaObject.connectSlotsByName(FormExit)

        self.addFunctions()

    def retranslateUi(self, FormExit):
        _translate = QtCore.QCoreApplication.translate
        FormExit.setWindowTitle(_translate("FormExit", "MainWindow"))
        self.lblExit.setText(_translate("FormExit", "Do you want exit?"))
        self.btnExit.setText(_translate("FormExit", "Exit"))
        self.btnGoMainWindow.setText(_translate("FormExit", "Go Main Window"))

    def addFunctions(self):
        self.btnExit.clicked.connect(lambda: self.Exit())
        self.btnGoMainWindow.clicked.connect(lambda: self.GoMainWindow())

    def Exit(self):
        print("The user is logout.")
        sys.exit()

    def GoMainWindow(self):
        FormExit.close()
        print("The user is logout.")
        MainWindow.show()


if __name__ == "__main__":
    import sys
    import rsa

    keysize = 32
    if (rsa.checkRSAData() != True):
        e, d, N = rsa.generateKeys(keysize)
    else:
        e, d, N = rsa.getRSAData()

    app = QtWidgets.QApplication(sys.argv)

    FormPersonalAccount = QtWidgets.QMainWindow()
    ui = Ui_FormPersonalAccount()
    ui.setupUi(FormPersonalAccount)

    FormExit = QtWidgets.QMainWindow()
    ui = Ui_FormExit()
    ui.setupUi(FormExit)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



