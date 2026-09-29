# Task Management System

A simple Flask web application for managing team tasks. The application allows users to create, view, update, search, change status, and delete tasks. Task data is stored in a JSON file for persistence.

## Features

* Create new tasks
* View all tasks
* View complete task details
* Update task title, description, and priority
* Change task status
* Set task priority as Low, Medium, or High
* Search tasks by title or description
* Delete tasks
* Store tasks in a JSON file
* Load saved tasks when the application starts
* Custom 404 page

## Technologies Used

* Python
* Flask
* Jinja2
* HTML
* CSS
* JSON
* uv

## Project Structure

```text
task-management/
├── src/
│   └── task_management/
│       ├── app.py
│       ├── data.py
│       ├── tasks.json
│       │
│       ├── routes/
│       │   ├── main.py
│       │   └── task.py
│       │
│       ├── templates/
│       │   ├── base.html
│       │   ├── index.html
│       │   ├── tasks.html
│       │   ├── task_details.html
│       │   ├── create_task.html
│       │   ├── update_task.html
│       │   ├── search.html
│       │   ├── status.html
│       │   └── 404.html
│       │
│       └── static/
│           └── style.css
│
├── pyproject.toml
└── uv.lock
```

## Requirements

* Python 3.12 or newer
* uv

## Installation

Create a virtual environment:

```bash
uv venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\activate
```

Install Flask:

```bash
uv add flask
```

## Running the Application

Move into the application directory:

```powershell
cd src\task_management
```

Run the application:

```powershell
uv run python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## Features

### Create Task

Users can create a task by providing:

* Task ID
* Title
* Description
* Status
* Priority

### View Tasks

The tasks page displays all available tasks with their:

* Task ID
* Title
* Description
* Status
* Priority

### Task Details

Each task has a separate details page where the complete task information can be viewed.

### Update Task

Users can update:

* Title
* Description
* Priority

The Task ID remains unchanged.

### Change Status

A task can have one of the following statuses:

```text
Pending
In Progress
Completed
```

### Priority

Each task can have one of the following priorities:

```text
Low
Medium
High
```

### Search

Tasks can be searched using words from the task title or description.

### Delete

Tasks can be deleted from the task list.

## JSON Persistence

Task data is stored in `tasks.json`.

When the application starts, the saved tasks are loaded from the JSON file.

When a task is created, updated, deleted, or its status is changed, the updated data is saved back to the JSON file.

The data flow is:

```text
tasks.json
    ↓
load_tasks()
    ↓
Python tasks list
    ↓
Flask application
    ↓
save_tasks()
    ↓
tasks.json
```

## Main Routes

| Method    | Route                    | Description        |
| --------- | ------------------------ | ------------------ |
| GET       | `/`                      | Home page          |
| GET       | `/tasks`                 | View all tasks     |
| GET, POST | `/create-task`           | Create a task      |
| GET       | `/task/<task_id>`        | View task details  |
| GET, POST | `/update-task/<task_id>` | Update a task      |
| GET       | `/search`                | Search tasks       |
| GET, POST | `/status/<task_id>`      | Change task status |
| POST      | `/delete-task/<task_id>` | Delete a task      |

## Project Structure Explanation

`app.py` creates the Flask application, registers the Blueprints, and handles the 404 page.

`data.py` stores the task data and manages loading and saving tasks to `tasks.json`.

`routes/main.py` contains the home page route.

`routes/task.py` contains all task-related routes.

`templates/` contains the Jinja2 HTML templates.

`static/` contains the CSS used to style the application.

## License

This project was created as a Flask learning and assignment project.
