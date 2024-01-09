def main():
    month = int(input("Введите номер месяца "))
    day = int(input("Введите день "))
    if day != max_day(month):
        next_day = day + 1
        next_month = month
    else:
        next_day = 1
        if month != 12:
            next_month = month + 1
        else:
            next_month = 1
    print(f"текущая дата - ({day}:{month}), следующая дата - ({next_day}:{next_month})")


def max_day(month):
    match month:
        case 1:
            return 31
        case 2:
            return 28
        case 3:
            return 31
        case 4:
            return 30
        case 5:
            return 31
        case 6:
            return 30
        case 7:
            return 31
        case 8:
            return 31
        case 9:
            return 30
        case 10:
            return 31
        case 11:
            return 30
        case 12:
            return 31
        case _:
            return 0


if __name__ == "__main__":
    main()
