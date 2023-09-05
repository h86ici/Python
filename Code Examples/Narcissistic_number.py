'''水仙花數也被稱為超完全數字不變數、自戀數、自冪數、阿姆斯特朗數，它是一個3位數，該數字每個位上數字的立方之和正好等於它本身，例如： 1^3 + 5^3+ 3^3=153。
'''

for num in range(100, 1000):
    first_digit = num % 10
    second_digit = num // 10 % 10
    third_digit = num // 100
    if num == first_digit ** 3 + second_digit ** 3 + third_digit ** 3:
        print(num)