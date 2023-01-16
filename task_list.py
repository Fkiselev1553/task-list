task_list = []


def add_task(task):
	while True:
		task = input("Введите задачу: ")
			if task == "1":
				break
		task_list.append(task)
		print("Задача", task, "добавлена")

def view_list():
	print("Список задач: ")
	for task in task_list:
		print(task)

def remove_task(task):
	task_list.remove(task)
	print("Задача", task, "удалена из вашего списка задач")
