import random

def generate_code(code_len = 4):
    """
    生成指定長度的驗證碼

    :param code_len: 驗證碼的長度(default 4 characters)

    :return: 由大小寫英文字母和數字構成的隨機驗證碼
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(0, code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

if __name__ == '__main__':
    generate_code()

