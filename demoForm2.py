#demoForm2.py
#demoForm2.ui (화면단) +  demoForm2.py (로직단)
#QyQt5 선언
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

#디자인한 파일을 로딩(demoForm2.ui)
form_class = uic.loadUiType("demoForm2.ui")[0]

#폼클래스를 정의(QMainWindow클래스를 상속)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯매서드를 정의
    def firstClick(self):
        self.label.setText("첫번째 버튼 클릭")    
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭했습니다")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭~~~")

#직접 모듈을 실행했는지 진입점체크
if __name__ == "__main__":
    app= QApplication(sys.argv)  #QApplication 객체 생성
    demoForm = DemoForm()  #DemoForm 객체 생성
    demoForm.show()  #폼을 보여줌
    app.exec_()  #이벤트 루프를 시작
