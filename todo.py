import json
import sys
import os

DATA_FILE = "todos.json"

def load():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)

def save(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def add(text):
    todos = load()
    todos.append({"id": len(todos) + 1, "task": text, "done": False})
    save(todos)
    print(f"Added: {text}")

def list_tasks():
    todos = load()
    if not todos:
        print("No tasks yet.")
        return
    for t in todos:
        status = "✓" if t["done"] else "○"
        print(f"  [{t['id']}] {status} {t['task']}")

def done(id):
    todos = load()
    for t in todos:
        if t["id"] == int(id):
            t["done"] = True
            save(todos)
            print(f"Done: {t['task']}")
            return
    print(f"Task {id} not found.")

def delete(id):
    todos = load()
    todos = [t for t in todos if t["id"] != int(id)]
    save(todos)
    print(f"Deleted task {id}.")

USAGE = """Usage:
  python todo.py add "task text"
  python todo.py list
  python todo.py done <id>
  python todo.py delete <id>"""

if len(sys.argv) < 2:
    print(USAGE)
elif sys.argv[1] == "add" and len(sys.argv) > 2:
    add(sys.argv[2])
elif sys.argv[1] == "list":
    list_tasks()
elif sys.argv[1] == "done" and len(sys.argv) > 2:
    done(sys.argv[2])
elif sys.argv[1] == "delete" and len(sys.argv) > 2:
    delete(sys.argv[2])
else:
    print(USAGE)
