import os
from datetime import datetime, timedelta

def rename_md_files_to_past_dates():
    folder_path = os.getcwd()
    files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
    files.sort()  # 파일명을 정렬하여 처리 순서를 보장

    today = datetime.now()
    files_per_day = 20

    for i, filename in enumerate(files):
        # 날짜 계산
        days_offset = i // files_per_day
        current_date = today - timedelta(days=days_offset)
        
        # 새로운 파일명 생성
        new_filename = current_date.strftime(f"%Y-%m-%d-{filename[11:]}")
        file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        
        # 파일명 변경
        os.rename(file_path, new_file_path)
        # print(f"Renamed file: {filename} -> {new_filename}")
    
    print("끝")

# 함수 실행
rename_md_files_to_past_dates()