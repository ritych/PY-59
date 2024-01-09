def main():
    first_number = int(input("Введите первое число "))
    second_number = int(input("Введите второе число "))
    operation = input("Введите операцию (+, -, *, /) ")

    print(f"{calculate(first_number, second_number, operation)}")


def calculate(a, b, op):
    match op:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            try:
                return a / b
            except:
                return "Ошибка: деление на 0"
        case _:
            return "Операция не поддерживается"


if __name__ == "__main__":
    main()
