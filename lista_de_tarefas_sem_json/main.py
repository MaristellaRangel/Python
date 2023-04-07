import todo_list_functions as td
todo = []
undo = []

while True:
    print("Commands: list, undo, redo, exit")
    inp = input("Enter a task or command: ").upper()
    if len(inp) == 0:
        print("Please enter a value")
    else:
        if isinstance(inp, str):
            if inp == 'LIST':
                print("TASKS:")
                td.list(todo)
            elif inp == 'UNDO':
                td.undo(todo, undo)
                td.list(todo)
            elif inp == 'REDO':
                td.redo(todo, undo)
                td.list(todo)
            elif inp == 'EXIT':
                break
            else:
                td.add_task(inp, todo)
                td.list(todo)
        else:
            print("Please, enter a string")
        print()
