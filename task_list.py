import json
import datetime
import random

# Параметры задачи
class Task:
    def __init__(self, name, due_date, status):
        self.name = name
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f'{self.name} - Дата: {self.due_date} - Статус Задачи: {self.status}'


tasks = []

# добавление задачи
def add_task():
    task_name = input("Введите задачу: ")
    due_date = input("Введите время до выполнения задачи в следующем формате: (YYYY-MM-DD): ")
    task_due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
    task_status = input("Введите статус задания: ")
    tasks.append(Task(task_name, task_due_date, task_status))
    print('Задача - ', task_name,  ' - была успешно добавлена!')

# эдит задачи
def edit_task():
    task_name = input("Введите задачу, которую хотите изменить: ")
    task_to_edit = None
    for task in tasks:
        if task.name == task_name:
            task_to_edit = task
            break
    if task_to_edit:
        task_name = input("Введите новое название задачи: ")
        task_to_edit.name = task_name
        due_date = input("Введите новую дату задачи (YYYY-MM-DD): ")
        task_to_edit.due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
        task_status = input("Введите новый статус задачи: ")
        task_to_edit.status = task_status
        print("Задача - ", task_name,  ' - успешно отредактирована!')
    else:
        print('Задача - ', task_name,  ' - не найдена')

# удалить задачу
def delete_task():
    task_name = input("Введите название задачи, которую хотите удалить: ")
    task_to_delete = None
    for task in tasks:
        if task.name == task_name:
            task_to_delete = task
            break
    if task_to_delete:
        tasks.remove(task_to_delete)
        print("Задача - ", task_name, " - была успешно удалена!" )
    else:
        print("Задача - ", task_name, " - не была найдена!")

#сохранить задачу в файл через  json
def save_to_file(tasks):
    with open("tasks.json", "w") as f:
        json.dump([task.__dict__ for task in tasks], f)

# извлечь список задач из файла
def read_from_file():
    with open("tasks.json", "r") as f:
        tasks_data = json.load(f)
    return [Task(task["name"], task["due_date"], task["task"]) for task in tasks_data]

# основной цикл
while True:
    print("1. Добавить задачу")
    print("2. Отредактировать задачу")
    print("3. Удалить задачу")
    print("4. Отобразить все задачу")
    print("5. Сохранить все задачи в файл")
    print("6. Загрузить задачи из файла")
    print("7. Выход")
    choice = input("Выберите, что хотите сделать (1-7): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        edit_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        tasks.sort(key=lambda x: (x.due_date, x.status))
        for task in tasks:
            print(task)
    elif choice == "5":
        save_to_file(tasks)
        print("Все задачи были успешно сохранены")
    elif choice == "6":
        tasks = read_from_file()
        print("Все задачи были успешно сохранены из файла")
    elif choice == "7":
        break
    else:
        answer_choices = ["Пожалуйста, попробуйте ещё раз!", "Попробуйте ещё раз!", "Неправильный вариант ответа, попробуйте ещё раз"]
        print(random.choice(answer_choices))

