# 简单数字计算器 (0-9)
# 支持加减乘除运算，限制输入为 0–9 之间的整数

def main():
    print("简单数字计算器 (0-9)")
    try:
        a = int(input("输入第一个数字 (0-9): "))
        if a < 0 or a > 9:
            print("数字必须在 0-9 之间")
            return

        b = int(input("输入第二个数字 (0-9): "))
        if b < 0 or b > 9:
            print("数字必须在 0-9 之间")
            return

        op = input("输入运算符 (+, -, *, /): ")

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                print("除数不能为零")
                return
            result = a / b
        else:
            print("无效运算符")
            return

        print(f"结果: {result}")
    except ValueError:
        print("输入无效，请输入整数")

if __name__ == '__main__':
    main()
