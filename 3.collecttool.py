
import time
import os
import natsort
start_time = time.time()

# 텍스트 파일이 모여있는 폴더
directory = 'yolov5/runs/detect/exp23/labels'

# 결과 파일명 지정
outfile_name = "itsme.txt"

# 결과 파일 생성
out_file = open(outfile_name, 'w')

# 폴더 내용물 목록 생성
#input_files1 = os.listdir(directory)

# 파일 순서대로 정렬, 목록생성 동시
input_files = natsort.natsorted(os.listdir(directory))
print(input_files)

# 폴더 내용을 하나하나 읽어 하나로 합치는 반복문 
for filename in input_files:
    if ".txt" not in filename:
        continue
    file = open(directory + "/" + filename)

    # 파일 내용 문자열로 저장
    content = file.read()

    # 문자열로 저장된 내용을 파일에 쓰기
    out_file.write(content)
    file.close()
out_file.close()
