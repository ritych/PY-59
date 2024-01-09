def main():
    first_number = int(input("Введите первое число "))
    second_number = int(input("Введите второе число "))
    third_number = int(input("Введите третье число "))
    print('Наименьшее число', find_minimum(first_number, second_number, third_number))


def find_minimum(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


if __name__ == "__main__":
    main()
