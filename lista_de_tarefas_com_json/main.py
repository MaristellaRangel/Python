import todo_list_functions as td
import todo_json_functions as tdj

lists = tdj.get_lists()
todo = lists[0]
undo = lists[1]

while True:
    print("Commands: list, undo, redo, exit")
    inp = input("Enter a task or command: ").upper()
    if len(inp) == 0:
        print("Please enter a value")
    else:
        if inp == 'LIST':
            print("TASKS:")
            td.list(todo)
        elif inp == 'UNDO':
            td.undo(todo, undo)
            tdj.set_lists(undo, todo)
            td.list(todo)
        elif inp == 'REDO':
            td.redo(todo, undo)
            tdj.set_lists(undo, todo)
            td.list(todo)
        elif inp == 'EXIT':
            break
        else:
            td.add_task(inp, todo)
            tdj.set_lists(undo, todo)
            td.list(todo)
        print()
