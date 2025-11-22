def number_valid_input(message: str):
    while True:
        try:
            num = float(input(message))
            if num <= 0:
                raise ValueError("аргумен не может быть меньше или равен нулю!")
            return num
        except (ValueError, TypeError) as ex:
            print(f"Ошибка: {ex}")


sallary = number_valid_input("Ведите заработную плату в месяц:")
proc_sallary1 = number_valid_input("Введите, какой процент(%) уходит на ипотеку:")
proc_sallary2 = number_valid_input("Введите, какой процент(%) уходит на жизнь:")
print(f"Вывод:\nНа ипотеку было потрачено:{sallary * proc_sallary1 / 100}")
print(f"Вывод:\nБыло накоплено {(1 - (proc_sallary1 + proc_sallary2) / 100) * sallary}")
