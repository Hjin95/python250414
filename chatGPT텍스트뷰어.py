import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QFileDialog, QWidget


class TextFileViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 윈도우 설정
        self.setWindowTitle("텍스트 파일 뷰어")
        self.setGeometry(100, 100, 800, 600)

        # 중앙 위젯 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 레이아웃 설정
        layout = QVBoxLayout()

        # 텍스트 박스
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)  # 읽기 전용으로 설정
        layout.addWidget(self.text_edit)

        # 파일 열기 버튼
        self.open_button = QPushButton("파일 열기", self)
        self.open_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_button)

        # 레이아웃을 중앙 위젯에 설정
        central_widget.setLayout(layout)

    def open_file(self):
        # 파일 열기 대화 상자
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "텍스트 파일 열기", "", "텍스트 파일 (*.txt);;모든 파일 (*)", options=options)

        if file_path:
            try:
                # 파일 내용 읽기
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                self.text_edit.setText(content)  # 텍스트 박스에 내용 표시
            except Exception as e:
                self.text_edit.setText(f"파일을 열 수 없습니다: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = TextFileViewer()
    viewer.show()
    sys.exit(app.exec_())