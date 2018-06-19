"""
111171103090 杨雯  2018.6.19
"""
def change(n):
    result = '0'
    if n == 0:    # 输入为0的情况
        return result
    else:
        result = change(n // 2)         # 调用自身
        return result + str(n % 2)
num = int(input("请输入要转换进制的数值："))  # 提示用户输入十进制数，由于input()的返回值是str类型，故需要转化为int类型

new_number = change(num)
if new_number[0] == '0':
    new_number = new_number[1:]

print("该数字转换为二进制后是",new_number)