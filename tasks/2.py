# 2. Какие ты видишь проблемы в следующем фрагменте кода?
# Как его следует исправить?
# Исправь ошибку и перепиши код с использованием типизвции.

##########################################################
# Изначальный код
def create_handlers(callback):
    handlers = []
    for step in range(5):
        # добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda: callback(step))
    return handlers

def execute_handlers(handlers):
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()
##########################################################

# 1) Код работает неправильно
# 2) Код ужасен

cb = print

handlers = create_handlers(cb)
execute_handlers(handlers)
# > 4
# > 4
# > 4
# > 4
# > 4

##########################################################
# Исправленный вариант
from typing import Any, Callable, List, NoReturn

cb_type = Callable[[Any], NoReturn]

def create_handlers(callback: cb_type) -> List[cb_type]:
    handlers = []
    for step in range(5):
        # создаем промежуточную лямюда-функцию cbx для связывания
        # колбэка с текущим значением step(каррирование)
        cbx = lambda step: lambda: callback(step)
        handlers.append(cbx(step))
    return handlers

def execute_handlers(handlers: List[cb_type]) -> None:
    for handler in handlers:
        handler()
handlers = create_handlers(cb)
execute_handlers(handlers)
# > 0
# > 1
# > 2
# > 3
# > 4
##########################################################
# Варианты дальнейших улучшений

# В качестве улучшения в функции create_handlers можно вынести количество шагов в аргумент
# функции, избавиться от лямбд(при отладке вместо имени функции отображается только <lambda function>) и добавить передачу списка списков аргументов для колбэков и список колбэков
# на случай ошибки в одном или нескольких хэндлерах.

# В качестве улучшения в функции execute_handlers можно добавить возможность ленивого вычисления, параллельное или асинхронное исполнение хэндлеров.

# В общем стоит добавить doc-строки и doc-тесты + юнит-тестирование
# С радостью бы это продемонстрировал, но не здесь
