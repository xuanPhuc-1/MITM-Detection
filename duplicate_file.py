import pandas as pd


def duplicate_rows(input_file, output_file, num_duplicates):
    # Đọc dữ liệu từ file CSV vào DataFrame
    df = pd.read_csv(input_file)

    # Nhân đôi DataFrame theo số lượng yêu cầu
    df_duplicated = pd.concat([df] * num_duplicates, ignore_index=True)

    # Lưu DataFrame đã được xử lý vào file CSV mới
    df_duplicated.to_csv(output_file, index=False)


# Sử dụng hàm với các tham số tương ứng
input_file_path = 'features-file-2.csv'
output_file_path = 'dataset.csv'
num_duplicates = 10  # Số lần nhân đôi, để nhân đôi số lượng dòng, đặt giá trị này là 2

duplicate_rows(input_file_path, output_file_path, num_duplicates)
