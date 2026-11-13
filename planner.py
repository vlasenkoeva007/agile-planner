"""
Agile Planner — планировщик Agile для личного пользования.
Учебный проект по дисциплине «Проектная деятельность в ИТ».
"""
import json
import os

DATA_FILE = "tasks.json"
STATUSES = ["backlog", "in progress", "done"]
PRIORITIES = ["low", "medium", "high"]


def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def next_id(tasks):
    return max((t["id"] for t in tasks), default=0) + 1


def add_task(tasks, title, priority):
    tasks.append({"id": next_id(tasks), "title": title,
                  "priority": priority, "status": "backlog"})
    print(f"Задача #{next_id(tasks) - 1} добавлена в Backlog.")


def show_board(tasks):
    for status in STATUSES:
        print(f"\n=== {status.upper()} ===")
        column = [t for t in tasks if t["status"] == status]
        if not column:
            print("  (пусто)")
        for t in column:
            print(f'  #{t["id"]} [{t["priority"]}] {t["title"]}')


def move_task(tasks, task_id, new_status):
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = new_status
            print(f'Задача #{task_id} перемещена в "{new_status}".')
            return
    print("Задача не найдена.")


def main():
    tasks = load_tasks()
    while True:
        print("\n1 - добавить задачу; 2 - показать доску; "
              "3 - переместить задачу; 0 - выход")
        choice = input("Ваш выбор: ").strip()
        if choice == "1":
            title = input("Название задачи: ").strip()
            priority = input(f"Приоритет {PRIORITIES}: ").strip().lower()
            if priority not in PRIORITIES:
                priority = "medium"
            add_task(tasks, title, priority)
        elif choice == "2":
            show_board(tasks)
        elif choice == "3":
            show_board(tasks)
            task_id = int(input("ID задачи: "))
            new_status = input(f"Новый статус {STATUSES}: ").strip().lower()
            if new_status in STATUSES:
                move_task(tasks, task_id, new_status)
            else:
                print("Неверный статус.")
        elif choice == "0":
            save_tasks(tasks)
            print("Данные сохранены. Выход.")
            break
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()
