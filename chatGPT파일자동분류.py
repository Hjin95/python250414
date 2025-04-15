import os
import shutil
from pathlib import Path

# 다운로드 폴더 경로
download_dir = Path(r"C:\Users\student\Downloads")

# 이동 대상 폴더 (필요 시 생성됨)
folders = {
    "images": [".jpg", ".jpeg"],
    "data": [".csv", ".xlsx"],
    "docs": [".txt", ".doc", ".pdf"],
    "archive": [".zip"]
}

# 파일 확장자를 소문자로 비교하도록 설정
extension_map = {}
for folder, extensions in folders.items():
    for ext in extensions:
        extension_map[ext.lower()] = folder

# 각 폴더 존재하지 않으면 생성
for folder in folders.keys():
    target_path = download_dir / folder
    if not target_path.exists():
        target_path.mkdir()
        print(f"📂 폴더 생성됨: {target_path}")

# 다운로드 폴더 안의 모든 파일 확인
for file in download_dir.iterdir():
    if file.is_file():
        ext = file.suffix.lower()
        if ext in extension_map:
            target_folder = download_dir / extension_map[ext]
            target_path = target_folder / file.name

            # 이름이 겹칠 경우 덮어쓰기 방지 (파일명 뒤에 숫자 붙이기)
            count = 1
            while target_path.exists():
                new_name = f"{file.stem}_{count}{file.suffix}"
                target_path = target_folder / new_name
                count += 1

            shutil.move(str(file), str(target_path))
            print(f"✅ 이동됨: {file.name} → {target_path}")
