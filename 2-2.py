def main():
    month = int(input("Введите номер месяца "))
    match month:
        case 1:
            print('в январе 31 день')
        case 2:
            print('в феврале 28 дней')
        case 3:
            print('в марте 31 день')
        case 4:
            print('в апреле 30 дней')
        case 5:
            print('в мае 31 день')
        case 6:
            print('в июне 30 дней')
        case 7:
            print('в июле 31 день')
        case 8:
            print('в августе 31 день')
        case 9:
            print('в сентябре 30 дней')
        case 10:
            print('в октябре 31 день')
        case 11:
            print('в ноябре 30 дней')
        case 12:
            print('в декабре 31 день')
        case _:
            print('ошибка')


if __name__ == "__main__":
    main()
