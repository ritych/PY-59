def number_to_words(num):
    hundreds = {1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'}
    tens = {2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}
    ones = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    teens = {10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}

    hundreds_digit = num // 100
    tens_digit = (num % 100) // 10
    ones_digit = num % 10

    description = ''
    if hundreds_digit > 0:
        description += hundreds[hundreds_digit] + ' '
    if tens_digit == 1:
        description += teens[num % 100]
    else:
        if tens_digit > 1:
            description += tens[tens_digit] + ' '
        if ones_digit > 0:
            description += ones[ones_digit]
    return description


def main():
    number = int(input("Введите число от 100 до 999 "))
    print(number, '—', number_to_words(number))


if __name__ == "__main__":
    main()
