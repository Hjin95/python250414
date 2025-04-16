#demoForm.py
#demoForm.ui (화면단) +  demoForm.py (로직단)
#QyQt5 선언
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

#디자인한 파일을 로딩
form_class = uic.loadUiType("demoForm.ui")[0]

#폼클래스를 정의(qdialog클래스를 상속)
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("문자열을 출력~~~")  #라벨에 텍스트를 출력

#직접 모듈을 실행했는지 진입점체크
if __name__ == "__main__":
    app= QApplication(sys.argv)  #QApplication 객체 생성
    demoForm = DemoForm()  #DemoForm 객체 생성
    demoForm.show()  #폼을 보여줌
    app.exec_()  #이벤트 루프를 시작
