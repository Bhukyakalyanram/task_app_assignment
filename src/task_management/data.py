import json
import os

FILE = os.path.join(os.path.dirname(__file__), "tasks.json")

tasks = [
    {
        "task_id": "T001",
        "title": "Complete Python Basics",
        "description": "Finish Python fundamentals exercises",
        "status": "Pending",
        "priority": "High",
    },
    {
        "task_id": "T002",
        "title": "Build Flask Page",
        "description": "Create the first Flask web page",
        "status": "In Progress",
        "priority": "Medium",
    },
    {
        "task_id": "T003",
        "title": "Learn Jinja2",
        "description": "Practice Jinja2 templates and loops",
        "status": "Pending",
        "priority": "Low",
    },
    {
        "task_id": "T004",
        "title": "Create GitHub Repo",
        "description": "Push the project to GitHub",
        "status": "Completed",
        "priority": "High",
    },
    {
        "task_id": "T005",
        "title": "Write Project README",
        "description": "Document how to run the application",
        "status": "Pending",
        "priority": "Medium",
    },
]


def load_tasks():
    global tasks

    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            tasks = json.load(file)


def save_tasks():
    with open(FILE, "w") as file:
        json.dump(tasks, file, indent=4)


load_tasks()
