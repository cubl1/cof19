class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = str(message)

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = str(message)

class Car:
    def __init__(self, model, vin, numbers):
        self.model = str(model)

        def __is_valid_numbers(number):
            if not isinstance(number, str):
                raise IncorrectCarNumbers("Некорректный тип данных для номеров")
            if len(number) != 6:
                raise IncorrectCarNumbers('Неверная длина номера')

        def __is_valid_vin(vin_number):
            if not isinstance(vin_number, int):
                raise IncorrectVinNumber('Некорректный тип vin номер')
            if vin_number < 1000000 or vin_number > 9999999:
                raise IncorrectVinNumber("Неверный диапазон для vin номера")

        __is_valid_vin(vin)
        __is_valid_numbers(numbers)

        self.__vin = vin
        self.__numbers = numbers

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
