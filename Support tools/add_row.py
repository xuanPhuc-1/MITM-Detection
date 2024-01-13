import csv
import random

# Số lượng dòng bạn muốn tạo
num_rows = 10

# Đường dẫn đến file CSV
output_file_path = 'dataset-real.csv'

# Mở file CSV để ghi dữ liệu
with open(output_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Ghi tiêu đề
    writer.writerow(["aps", "abps", "subarp", "miss_mac", "class/"])

    # Ghi dữ liệu với giá trị ngẫu nhiên
    for _ in range(num_rows):
        aps = round(random.uniform(20.0, 30.0), 3)
        abps = round(random.uniform(3.0, 4.0), 3)
        subarp = int(random.uniform(1, 4))
        miss_mac = 1
        class_value = 1 
        writer.writerow([aps, abps, subarp, miss_mac, class_value])

print(f"File '{output_file_path}' đã được tạo thành công.")
