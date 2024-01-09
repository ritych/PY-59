def main():
    count = 0
    first_number = int(input("Введите первое число "))
    second_number = int(input("Введите второе число "))
    third_number = int(input("Введите третье число "))
    if first_number > 0:
        count += 1
    if second_number > 0:
        count += 1
    if third_number > 0:
        count += 1
    print("Положительных чисел", count)


if __name__ == "__main__":
    main()
