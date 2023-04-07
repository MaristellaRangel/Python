import json


def get_lists():
    with open("todo.json", 'r', encoding='utf8') as arquivo:
        content = json.load(arquivo)
        todo = content["todo"]
        undo = content["undo"]
        return todo, undo


def set_lists(undo_list, todo_list):
    with open('todo.json', 'w', encoding='utf8') as arquivo:
        content = {
            "todo" : todo_list,
            "undo" : undo_list
        }
        json.dump(content, arquivo)
