# Тема 1: Начало работы
# -------------------------------
# Git — это распределённая система контроля версий.
# Она позволяет отслеживать изменения в проекте и возвращаться к любому состоянию.
# Основная команда:
# git init — превращает обычную папку в репозиторий (создаёт скрытую папку .git).

# -------------------------------
# Тема 2: Создание репозитория
# -------------------------------
# Обычно команды выполняются в терминале:
# mkdir my_project         # создаём папку проекта
# cd my_project            # заходим в папку
# git init                # инициализация репозитория
# git status              # проверка статуса (что изменено, что не отслеживается)

# -------------------------------
# Тема 3: Заполнение репозитория
# -------------------------------
# Создаём файл:
# echo "print('Hello Git!')" > main.py
# Добавляем его в индекс:
# git add main.py
# Сохраняем в истории (делаем коммит):
# git commit -m "Initial commit: add main.py"

# -------------------------------
# Тема 4: Публикация изменений
# -------------------------------
# Публикация = коммит (фиксируем изменения).
# git add <файл>   # добавить файл в индекс
# git commit -m "Сообщение"  # сохранить изменения в истории

# -------------------------------
# Тема 5: Внесение изменений
# -------------------------------
# Изменяем файл:
# echo "print('Second version')" >> main.py
# git status    # Git увидит, что файл изменён
# git add main.py
# git commit -m "Added second line"

# -------------------------------
# Тема 6: Просмотр истории коммитов
# -------------------------------
# git log — показывает историю коммитов.
# Удобно использовать короткий формат:
# git log --oneline

# -------------------------------
# Тема 7: Просмотр конкретного коммита
# -------------------------------
# Скопировать хэш из git log (например abc123) и:
# git show abc123  # показать изменения этого коммита

# -------------------------------
# Тема 8: Возврат к предыдущему коммиту
# -------------------------------
# git checkout HEAD~1  # перейти на предыдущий коммит
# cat main.py          # проверяем, что файл вернулся к старому состоянию
# git checkout main    # вернуться на последнюю версию (главная ветка)

# -------------------------------
# Тема 9: Работа с историей изменений
# -------------------------------
# git diff       # показать, что изменилось с момента последнего коммита
# git log --stat # история + статистика (сколько строк изменилось)

# -------------------------------
# Тема 10: Создание ветки
# -------------------------------
# git branch feature   # создаём ветку
# git checkout feature # переключаемся на неё

# -------------------------------
# Тема 11: Переход между ветками
# -------------------------------
# git checkout main    # вернуться на главную ветку
# git checkout feature # снова в ветку feature

# -------------------------------
# Тема 12: Слияние веток
# -------------------------------
# Находясь в main, можно слить feature:
# git merge feature    # изменения из feature попадут в main

# -------------------------------
# Тема 13: Разрешение конфликтов
# -------------------------------
# Если одна и та же строка изменена в двух ветках,
# при merge Git сообщит о конфликте.
# Тогда нужно:
# 1. Открыть файл в редакторе
# 2. Выбрать, какие изменения оставить
# 3. git add main.py
# 4. git commit -m "Resolved merge conflict"


"""
============================
Лабораторная работа: Git + Python
============================

Раздел 1: Git (по GitHowTo)

1. Создание репозитория
# git init

2. Добавление файлов в индекс
# git add <file>

3. Создание коммита
# git commit -m "Сообщение коммита"

4. Проверка статуса репозитория
# git status

5. Просмотр истории коммитов
# git log

6. Просмотр различий
# git diff

7. Работа с ветками
# git branch <branch-name>

8. Переключение между ветками
# git checkout <branch-name>

9. Слияние веток
# git merge <branch-name>

10. Работа с удалёнными репозиториями
# git remote add origin <url>

11. Отправка изменений в удалённый репозиторий
# git push origin <branch-name>

12. Получение изменений из удалённого репозитория
# git pull origin <branch-name>

13. Клонирование удалённого репозитория
# git clone <url>


============================
Раздел 2: Python (W3Schools, HOME → Python Strings)
============================

1. Hello World
# print("Hello, World!")

2. Variables
# x = 5
# y = "John"
# print(x)
# print(y)

3. Data Types
# x = 5
# y = "John"
# print(type(x))
# print(type(y))

4. Numbers
# x = 5
# y = 2.5
# print(type(x))
# print(type(y))

5. Casting
# x = 5.5
# y = int(x)
# print(y)

6. Strings
# x = "Hello"
# y = 'World'
# print(x + " " + y)

7. Booleans
# x = True
# y = False
# print(type(x))
# print(type(y))

8. Operators
# x = 5
# y = 2
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)

9. Lists
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])

10. Tuples
# fruits = ("apple", "banana", "cherry")
# print(fruits[0])

11. Sets
# fruits = {"apple", "banana", "cherry"}
# print("banana" in fruits)

12. Dictionaries
# person = {"name": "John", "age": 36}
# print(person["name"])

13. If...Else
# x = 20
# if x > 18:
#     print("Adult")
# else:
#     print("Not an adult")

14. While Loops
# i = 1
# while i < 6:
#     print(i)
#     i += 1

15. For Loops
# for x in range(6):
#     print(x)

16. Functions
# def my_function():
#     print("Hello from a function")
# my_function()

17. Lambda Functions
# x = lambda a, b: a + b
# print(x(5, 3))

18. Arrays
# import array
# x = array.array('i', [1, 2, 3])
# print(x[1])

19. Classes
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)

20. String Methods
# txt = "Hello, World!"
# print(txt.lower())
# print(txt.upper())
# print(txt.strip())

21. String Formatting
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))
"""



print("hello world")