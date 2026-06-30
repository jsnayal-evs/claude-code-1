# CLI Todo App

A simple command-line todo list manager built with Python. Tasks persist between sessions using a local JSON file.

## Requirements

- Python 3.x (no external dependencies)

## Usage

```bash
# Add a new task
python todo.py add "Buy groceries"

# List all tasks
python todo.py list

# Mark a task as done
python todo.py done 1

# Delete a task
python todo.py delete 1
```

## Example

```
$ python todo.py add "Buy groceries"
Added: Buy groceries

$ python todo.py add "Read a book"
Added: Read a book

$ python todo.py list
  [1] ○ Buy groceries
  [2] ○ Read a book

$ python todo.py done 1
Done: Buy groceries

$ python todo.py list
  [1] ✓ Buy groceries
  [2] ○ Read a book

$ python todo.py delete 2
Deleted task 2.
```

## Data Storage

Tasks are saved to `todos.json` in the same directory. This file is excluded from version control via `.gitignore`.
