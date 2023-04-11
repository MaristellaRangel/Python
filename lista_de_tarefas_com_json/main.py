import todo_list_functions as td
import todo_json_functions as tdj

file = 'to_do.json'
lists = tdj.get_lists(file)
todo = lists[0]
undo = lists[1]

while True:
    print("Commands: list, undo, redo, delete (cannot be undone), exit")
    inp = input("Enter a task or command: ").upper()
    if len(inp) == 0:
        print("Please enter a value")
    else:
        if inp == 'LIST':
            print("TASKS:")
        elif inp == 'UNDO':
            td.undo(todo, undo)
        elif inp == 'REDO':
            td.redo(todo, undo)
        elif inp == 'DELETE':
            td.delete_task(todo, undo)
        elif inp == 'EXIT':
            break
        else:
            td.add_task(inp, todo)
        print()
        tdj.set_lists(file, undo, todo)
        td.list(todo)

