def verify_task_in_list(task, list):
    if task not in list:
        return True
    return False


def add_task(task, list):
    if verify_task_in_list(task, list):
        task.upper()
        list.append(task)
    else:
        print("Task is already in list!")


def delete_task(list):
    task = get_task_to_delete()
    task = task.upper()
    if task in list:
        list.remove(task)
    else:
        print("Task not found")


def get_task_to_delete():
    task = input('task: ')
    return task

def verify_length_zero(list):
    if len(list) == 0:
        return True
    return False


def list(list):
    print(*list, sep='\n')


def undo(todo_list, undo_list):
    if verify_length_zero(todo_list):
        print("Nothing to undo!")
    else:
        task_to_undo = todo_list[-1]
        add_task(task_to_undo, undo_list)
        todo_list.pop()


def redo(todo_list, undo_list):
    if verify_length_zero(undo_list):
        print("Nothing to redo")
    else:
        task_to_redo = undo_list[-1]
        add_task(task_to_redo, todo_list)
        undo_list.pop()
