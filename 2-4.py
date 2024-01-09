def main():
    direction = input("Введите направление (допустимые значения N, W, E, S) ")
    command = int(input("Введите команду "))
    match command:
        case 0:
            print('продолжаем движение')
            print(f'Текущее направление не изменилось - {direction}')
        case 1:
            print('поворот налево')
            if direction == 'N':
                new_direction = 'W'
                print(f'Новое направление - {new_direction}')
            elif direction == 'W':
                new_direction = 'S'
                print(f'Новое направление - {new_direction}')
            elif direction == 'S':
                new_direction = 'E'
                print(f'Новое направление - {new_direction}')
            else:
                new_direction = 'N'
                print(f'Новое направление - {new_direction}')
        case -1:
            print('поворот направо')
            match direction:
                case 'N':
                    new_direction = 'E'
                    print(f'Новое направление - {new_direction}')
                case 'W':
                    new_direction = 'N'
                    print(f'Новое направление - {new_direction}')
                case 'S':
                    new_direction = 'W'
                    print(f'Новое направление - {new_direction}')
                case 'E':
                    new_direction = 'S'
                    print(f'Новое направление - {new_direction}')
        case _:
            print('Команада не поддерживается')


if __name__ == "__main__":
    main()
