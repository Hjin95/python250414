import random
from openpyxl import Workbook

# 엑셀 워크북 생성
wb = Workbook()
ws = wb.active
ws.title = "제품리스트"

# 헤더 추가
ws.append(["제품 ID", "제품명", "수량", "가격"])

# 샘플 데이터 생성
product_names = [
    "스마트폰", "노트북", "태블릿", "스마트워치", "헤드폰", 
    "스피커", "키보드", "마우스", "모니터", "프린터"
]

for i in range(1, 101):  # 100개의 데이터 생성
    product_id = f"P{i:03d}"  # 제품 ID (예: P001, P002, ...)
    product_name = random.choice(product_names)  # 랜덤 제품명 선택
    quantity = random.randint(1, 50)  # 수량 (1~50 랜덤)
    price = random.randint(10000, 1000000)  # 가격 (1만~100만 랜덤)
    ws.append([product_id, product_name, quantity, price])

# 엑셀 파일 저장
wb.save("products.xlsx")
print("products.xlsx 파일이 생성되었습니다.")