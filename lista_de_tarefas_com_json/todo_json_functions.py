import json


def get_lists(f):
    try:
        with open(f, 'r', encoding='utf8') as file:
            content = json.load(file)
    except FileNotFoundError:
        with open(f, 'w', encoding='utf8') as file:
            content = {"todo" : [], "undo": []}
            json.dump(content, file)
    finally:
        todo = content["todo"]
        undo = content["undo"]
        return todo, undo


def set_lists(f, undo_list, todo_list):
    with open(f, 'w', encoding='utf8') as file:
        content = {
            "todo" : todo_list,
            "undo" : undo_list
        }
        json.dump(content, file)
