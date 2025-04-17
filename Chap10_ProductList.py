import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic
import sqlite3
import os.path

# 데이터베이스 관리 클래스
class DatabaseManager:
    def __init__(self, db_name="ProductList.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.initialize_database()

    def initialize_database(self):
        """데이터베이스 초기화 및 테이블 생성"""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Price INTEGER NOT NULL
            );
        """)
        self.connection.commit()

    def execute_query(self, query, params=()):
        """쿼리 실행"""
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_all(self, query, params=()):
        """모든 데이터 가져오기"""
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close_connection(self):
        """데이터베이스 연결 닫기"""
        if self.connection:
            self.connection.close()


# 디자인 파일 로딩 (ProductList.ui)
form_class = uic.loadUiType("ProductList.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 데이터베이스 매니저 초기화
        self.db_manager = DatabaseManager()

        # 초기값 설정
        self.id = 0
        self.name = ""
        self.price = 0

        # QTableWidget 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.doubleClicked.connect(self.doubleClick)

        # 엔터키로 다음 컨트롤로 이동
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())

        # 초기 데이터 로드
        self.getProduct()

    def addProduct(self):
        """제품 추가"""
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        if self.name and self.price.isdigit():
            self.db_manager.execute_query(
                "INSERT INTO Products (Name, Price) VALUES (?, ?);",
                (self.name, int(self.price))
            )
            self.getProduct()
        else:
            QMessageBox.warning(self, "입력 오류", "제품명과 가격을 올바르게 입력하세요.")

    def updateProduct(self):
        """제품 수정"""
        self.id = self.prodID.text()
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        if self.id.isdigit() and self.name and self.price.isdigit():
            self.db_manager.execute_query(
                "UPDATE Products SET Name = ?, Price = ? WHERE id = ?;",
                (self.name, int(self.price), int(self.id))
            )
            self.getProduct()
        else:
            QMessageBox.warning(self, "입력 오류", "올바른 데이터를 입력하세요.")

    def removeProduct(self):
        """제품 삭제"""
        self.id = self.prodID.text()
        if self.id.isdigit():
            self.db_manager.execute_query(
                "DELETE FROM Products WHERE id = ?;",
                (int(self.id),)
            )
            self.getProduct()
        else:
            QMessageBox.warning(self, "입력 오류", "올바른 제품 ID를 입력하세요.")

    def getProduct(self):
        """제품 목록 가져오기"""
        self.tableWidget.clearContents()
        products = self.db_manager.fetch_all("SELECT * FROM Products;")
        self.tableWidget.setRowCount(len(products))
        for row, item in enumerate(products):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item[0])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(item[2])))

    def doubleClick(self):
        """테이블 더블 클릭 시 데이터 로드"""
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

    def closeEvent(self, event):
        """창 닫기 이벤트 처리"""
        self.db_manager.close_connection()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()




