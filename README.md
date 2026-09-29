# Task Management System

A beginner Flask web application that manages a team's daily tasks. Tasks are stored in a Python
list of dictionaries (no database) and displayed with Jinja2 templates.

## Requirements

- Python 3.10 or newer
- Flask 3.x

Install Flask:

```
uv add flask
```

## How to run

From inside the project folder, run this exact command:

```
python __init__.py
```

Then open the application in a browser:

```
http://127.0.0.1:5000
```

Stop the server with `Ctrl + C`.

## Project structure

```
task-management/
├── app.py
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── tasks.html
│   ├── create_task.html
│   ├── update_task.html
│   ├── search.html
│   ├── status.html
│   └── 404.html
└── static/
    └── style.css
```

## Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Home page and navigation |
| `/tasks` | GET | Show all tasks in a table |
| `/create-task` | GET, POST | Show and process the create-task form |
| `/update-task/<task_id>` | GET, POST | Show and process the update form |
| `/search` | GET | Search tasks by keyword |
| `/status/<task_id>` | GET, POST | Change the status of a task |
| `/delete-task/<task_id>` | GET, POST | Delete a task |

## Usage

1. **View tasks** — open `/tasks` to see the five sample tasks with their status.
2. **Create a task** — open `/create-task`, fill in Task ID, Title and Description, pick a status
   (Pending by default) and submit. Empty fields and duplicate Task IDs are rejected with a message.
3. **Update a task** — press *Update* on any row, change the title or description and save. The
   Task ID cannot be changed because it identifies the task.
4. **Change status** — pick a new status from the dropdown on the task row and press *Save*, or use
   the `/status/<task_id>` page. The three statuses are Pending, In Progress and Completed.
5. **Search** — open `/search` and type a word from a title or description. The search ignores
   upper and lower case. When nothing matches, the page says no tasks were found.
6. **Delete a task** — press *Delete* on the row. A confirmation message is shown.

If a Task ID in the URL does not exist (for example `/update-task/T999`), the application shows an
error message and returns to the task list.

## Notes

- Tasks are kept in memory, so restarting the server resets the list to the five sample tasks.
- `find_task(task_id)` is the shared helper used by the update, status and delete routes.
- Form input is read with `request.form`; the search keyword is read with `request.args`.
