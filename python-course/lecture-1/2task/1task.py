def number_valid_input(message: str):
    while True:
        try:
            num = float(input(message))
            if num <= 0:
                raise ValueError("аргумен не может быть меньше или равен нулю!")
            return num
        except (ValueError, TypeError) as ex:
            print(f"Ошибка: {ex}")


length_sq = number_valid_input("Введите длину стороны квадрата:")
print(f"Вывод:\nПериметр:\t{length_sq * 4}\nПлощадь:\t{length_sq**2}")

length_rec = number_valid_input("Введите длину прямоугольника:")
width_rec = number_valid_input("Введите ширину прямоугольника:")
print(
    f"Вывод:\nПериметр:\t{(length_rec + width_rec) * 2}\nПлощадь:\t{length_rec * width_rec}"
)
