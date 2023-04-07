def verify_task_in_list(task, list):
    if task not in list:
        return True
    return False


def add_task(task, list):
    if verify_task_in_list(task, list):
        list.append(task)


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
        add_task(todo_list[-1], undo_list)
        todo_list.pop()


def redo(todo_list, undo_list):
    if verify_length_zero(undo_list):
        print("Nothing to redo")
    else:
        add_task(undo_list[-1], todo_list)
        undo_list.pop()

