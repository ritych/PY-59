def main():
    mark = int(input("Введите оценку "))
    match mark:
        case 1:
            print('плохо')
        case 2:
            print('неудовлетворительно')
        case 3:
            print('удовлетворительно')
        case 4:
            print('хорошо')
        case 5:
            print('отлично')
        case _:
            print('ошибка')


if __name__ == "__main__":
    main()
