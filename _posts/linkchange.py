import os

# 현재 폴더의 모든 파일 중 .md 파일을 대상으로 작업
def replace_links_in_md_files():
    # 현재 폴더 경로
    folder_path = os.getcwd()

    # 폴더 내 모든 파일에 대해 반복
    for filename in os.listdir(folder_path):
        # 파일이 .md로 끝나는 경우에만 처리
        if filename.endswith('.md'):
            file_path = os.path.join(folder_path, filename)

            # 파일 읽기
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 특정 링크를 변경
            new_content = content.replace(
                'https://link.coupang.com/re/AFFSDP?lptag',
                'https://Robert4Johnsona.github.io?lptag'
            )

            # 변경된 내용을 동일한 파일에 저장
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)

            # print(f"Updated file: {filename}")
        print("끝")

# 함수 실행
replace_links_in_md_files()