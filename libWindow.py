""" 
    libWindowBase
"""

from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QLabel,QTextEdit

#----------------------------------------------------------------
#----------------------------------------------------------------
class WindowUtility(QWidget):
    def __init__(self, app:QApplication):
        super().__init__()
        self.app = app

        self.wx = 0
        self.wy = 0
        self.ww = 0
        self.wh = 0
        self.logs = None
        self.inputBox = None

    # UIの初期化
    def InitializeUI(self, title:str, x:int = 0, y:int = 0, w:int = 0, h:int = 0):
        self.wx = x if x != 0 else 300
        self.wy = y if y != 0 else 300
        self.ww = w if w != 0 else 620
        self.wh = h if h != 0 else 800

        self.setStyleSheet('font-family: Kaiti SC; font-size: 14px;')
        self.setWindowTitle(title) # ウィンドウのタイトル
        self.setGeometry(self.wx, self.wy, self.ww, self.wh) # ウィンドウの位置と大きさ

    #----------------------------------------------------------------
    # 汎用ボタン作成
    def createButton(self, name:str, x:int, y:int, w:int, h:int, delegate) -> QPushButton:
        button = QPushButton(name,self)
        button.pressed.connect(delegate)
        button.setGeometry(x,y,w,h)
        return button

    #----------------------------------------------------------------
    # 入力Box処理
    def createInputBox(self, title:str, x:int, y:int, w:int, h:int, delagate) -> QLineEdit:
        label = QLabel(title, self)
        label.setGeometry(10, y, 100, h)

        self.inputBox = QLineEdit('',self)
        self.inputBox.setGeometry(x, y, w, h)
        self.inputBox.returnPressed.connect(delagate)
        return self.inputBox

    # 入力エリアクリア
    def clearInput(self) -> None:
        if self.inputBox is not None:
            self.inputBox.setText("")

    #----------------------------------------------------------------
    # LogView処理
    def createLogView(self, x:int, y:int, w:int, h:int) -> QTextEdit:
        self.logs = QTextEdit(self)
        self.logs.setGeometry(x,y,w,h)
        return self.logs

    # LogViewhへの文字列追加
    def addLogMessage(self, newText) -> None:
        if self.logs is not None and newText != "":
            text = self.logs.toPlainText()
            text = newText + "\n" + text
            self.logs.setText(text)

    # LogClearボタン処理
    def clearLog(self) -> None:
        if self.logs is not None:
            self.logs.setText("")


    #----------------------------------------------------------------
    # main
    def main(self) -> None:
        self.showNormal()
        self.app.exec()

#----------------------------------------------------------------