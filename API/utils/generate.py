import random
import string

def generate_unique_class_code(list_code_class):
    while True:
        class_code = generate_random_string()
        if class_code not in list_code_class:
            return class_code


def generate_random_string(length=6):
    # Tạo một danh sách chứa tất cả các ký tự có thể được sử dụng
    characters = string.ascii_letters + string.digits
    # Sử dụng random.choice để chọn ngẫu nhiên 'length' ký tự từ danh sách
    random_chars = [random.choice(characters) for _ in range(length)]
    # Kết hợp các ký tự để tạo thành chuỗi
    random_string = ''.join(random_chars)

    return random_string

# Sử dụng hàm để tạo chuỗi ngẫu nhiên có độ dài là 6
# random_string = generate_random_string()
# print(random_string)
