# Задание №1. Написание программы.
# ==================================================================================================
print("""
# Задание №1. Написание программы.
# ==================================================================================================
""")
from Student import Student
from random import randint

from typing import Callable, List

students : List[Student] = [
  Student("Алексей", 20),
  Student("Владимир", 22),
  Student("Александр", 18),
  Student("Максим", 17),
  Student("Женя", 19),
  Student("Саша", 20),
  Student("Сергей", 20),
  Student("Олег", 18),
  Student("Наталья", 18),
  Student("Маша", 18),
  Student("Люда", 19),
  Student("Кристина", 19),
  Student("Сережа", 21),
  Student("Влад", 21),
  Student("Никита", 20),
  Student("Илья", 20),
  Student("Арсений", 19),
]


for student in students:
  student.mark = randint(0, 100)


# ====== Императивный стиль ====== #
print("# ====== Императивный стиль ====== #")

countOfStudents = 0
sumOfMarks = 0

for student in students:
  if student.age < 19:
    countOfStudents += 1
    sumOfMarks += student.mark

print("СРЕДНИЙ балл у студентов с возрастом < 19: ", sumOfMarks / countOfStudents)

maxMark = 0

for student in students:
  if student.age < 19:
    if student.mark > maxMark:
      maxMark = student.mark

print("МАКСИМАЛЬНЫЙ балл у студентов с возрастом < 19: ", maxMark)


# ====== Процедурный стиль ====== #
print("\n# ====== Процедурный стиль ====== #")
filteredStudents : List[Student] = []
averageMark = 0
maxMark = 0
countOfStudents = 0

def filterStudents():
  global filteredStudents, countOfStudents

  filteredStudents = []
  countOfStudents = 0

  for student in students:
    if student.age < 19:
      countOfStudents += 1
      filteredStudents.append(student)


def calculateAverageMark():
  global filteredStudents, averageMark, countOfStudents

  filterStudents()
  for student in filteredStudents:
    averageMark += student.mark

  averageMark /= countOfStudents

calculateAverageMark()
print("СРЕДНИЙ балл у студентов с возрастом < 19: ", averageMark)


def calculateMaxMark():
  global filteredStudents, maxMark

  filterStudents()
  for student in filteredStudents:
    if student.mark > maxMark:
      maxMark = student.mark

calculateMaxMark()
print("МАКСИМАЛЬНЫЙ балл у студентов с возрастом < 19: ", maxMark)


# ====== Функциональный стиль ====== #
print("\n# ====== Функциональный стиль ====== #")

def getAverageMark(predicate: Callable[[Student], bool]):
  filteredStudents : List[Student] = list(filter(predicate, students))
  return sum(map(lambda student: student.mark, filteredStudents)) / len(filteredStudents)

print("СРЕДНИЙ балл у студентов с возрастом < 19: ", end="")
print(getAverageMark(lambda student: student.age < 19))


def getMaxMark(predicate: Callable[[Student], bool]):
  filteredStudents : List[Student] = filter(predicate, students)
  return max(map(lambda student: student.mark, filteredStudents))

print("МАКСИМАЛЬНЫЙ балл у студентов с возрастом < 19: ", end="")
print(getMaxMark(lambda student: student.age < 19))

# ====== Функциональный стиль ====== #



# Задание №2. Вносим правки.
# ==================================================================================================
print("""\n
# Задание №2. Вносим правки.
# ==================================================================================================
""")
# ====== Императивный стиль ====== #
print("# ====== Императивный стиль ====== #")

countOfStudents = 0
sumOfMarks = 0

for student in students:
  if student.name.startswith("А"): # было student.age < 19
    countOfStudents += 1
    sumOfMarks += student.mark

print("СРЕДНИЙ балл у студентов, имя которых начинается на букву А: ", sumOfMarks / countOfStudents)

maxMark = 0

for student in students:
  if student.age < 19 and student.mark < 70: # добавил and student.mark < 70
    if student.mark > maxMark:
      maxMark = student.mark

print("МАКСИМАЛЬНЫЙ балл у студентов с возрастом < 19 и баллом < 70: ", maxMark)


# ====== Процедурный стиль ====== #
print("\n# ====== Процедурный стиль ====== #")
filteredStudents : List[Student] = []
averageMark = 0
maxMark = 0
countOfStudents = 0

def filterStudentsName():
  global filteredStudents, countOfStudents

  filteredStudents = []
  countOfStudents = 0

  for student in students:
    if student.name.startswith("А"):
      countOfStudents += 1
      filteredStudents.append(student)


def filterStudentsAgeAndMark():
  global filteredStudents, countOfStudents

  filteredStudents = []
  countOfStudents = 0

  for student in students:
    if student.age < 19 and student.mark < 70:
      countOfStudents += 1
      filteredStudents.append(student)


def calculateAverageMark():
  global filteredStudents, averageMark, countOfStudents

  filterStudentsName()
  for student in filteredStudents:
    averageMark += student.mark

  averageMark /= countOfStudents

calculateAverageMark()
print("СРЕДНИЙ балл у студентов, имя которых начинается на букву А: ", averageMark)


def calculateMaxMark():
  global filteredStudents, maxMark

  filterStudentsAgeAndMark()
  for student in filteredStudents:
    if student.mark > maxMark:
      maxMark = student.mark

calculateMaxMark()
print("МАКСИМАЛЬНЫЙ балл у студентов с возрастом < 19 и баллом < 70: ", maxMark)


# ====== Функциональный стиль ====== #
print("\n# ====== Функциональный стиль ====== #")

def getAverageMark(predicate: Callable[[Student], bool]):
  filteredStudents : List[Student] = list(filter(predicate, students))
  return sum(map(lambda student: student.mark, filteredStudents)) / len(filteredStudents)

print("СРЕДНИЙ балл у студентов, имя которых начинается на букву А: ", end="")
print(getAverageMark(lambda student: student.name.startswith("А"))) # Изменил условие в лямбда функции


def getMaxMark(predicate: Callable[[Student], bool]):
  filteredStudents : List[Student] = filter(predicate, students)
  return max(map(lambda student: student.mark, filteredStudents))

print("МАКСИМАЛЬНЫЙ балл у студентов с возрастом < 19 и баллом < 70: ", end="")
print(getMaxMark(lambda student: student.age < 19 and student.mark < 70)) # Изменил условие в лямбда функции