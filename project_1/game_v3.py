"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np

# Первая функция оставлена для сравнения конечного результата

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


# Вторая функция оставлена для сравнения конечного результата
def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count


# Третья доработанная функция
def game_core_v3(number: int=1) -> int:
    """Функция угадывает загаданное число, уменьшая или увеличивая
    предположение в зависимости от того, больше или меньше оно нужного.
    
    Args:
        number (int): Загаданное число.

    Returns:
        int: Число попыток.
    """
    count = 0
    minimum = 1 # Устанавливаем нижнюю границу загадываемого диапазона
    maximum = 100 # Устанавливаем верхнюю границу загадываемого диапазона
    
    predict = (minimum + maximum) // 2  # Определяем среднее значение

    # Цикл продолжается, пока предсказанное число не совпадет с загаданным
    while number != predict:
        count += 1
        if number > predict:
            minimum = predict + 1  # Обновляем нижнюю границу
        elif number < predict:
            maximum = predict - 1  # Обновляем верхнюю границу
        predict = (minimum + maximum) // 2  # Вычисляем новое предположение как среднее значение

    return count


# Функция для определния количества попыток, не дорабатывалась в проекте
def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score




#Проверяем работу всех алгоритмов (3 версии)
print('Run benchmarking for random_predict: ', end='')
score_game(random_predict)

print('Run benchmarking for game_core_v2: ', end='')
score_game(game_core_v2)

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)