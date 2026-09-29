from flask import Blueprint, render_template, request, redirect, url_for, flash
from data import tasks, save_tasks

task_bp = Blueprint("task", __name__)

STATUSES = ["Pending", "In Progress", "Completed"]
PRIORITIES = ["Low", "Medium", "High"]


def find_task(task_id):
    if not task_id:
        return None

    for task in tasks:
        if task["task_id"].lower() == task_id.strip().lower():
            return task

    return None


def validate_new_task(task_id, title, description):
    if not task_id:
        return "Task ID cannot be empty."

    if not title:
        return "Title cannot be empty."

    if not description:
        return "Description cannot be empty."

    if find_task(task_id):
        return "Task ID " + task_id + " already exists."

    return None


@task_bp.route("/tasks")
def view_tasks():
    return render_template("tasks.html", tasks=tasks, statuses=STATUSES)


@task_bp.route("/create-task", methods=["GET", "POST"])
def create_task():

    if request.method == "POST":

        task_id = request.form.get("task_id", "").strip()
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        status = request.form.get("status", "Pending").strip()
        priority = request.form.get("priority", "Medium").strip()

        if status not in STATUSES:
            status = "Pending"

        if priority not in PRIORITIES:
            priority = "Medium"

        error = validate_new_task(task_id, title, description)

        if error:
            flash(error, "error")

            return render_template(
                "create_task.html",
                statuses=STATUSES,
                priorities=PRIORITIES,
                form={
                    "task_id": task_id,
                    "title": title,
                    "description": description,
                    "status": status,
                    "priority": priority,
                },
            )

        tasks.append(
            {
                "task_id": task_id,
                "title": title,
                "description": description,
                "status": status,
                "priority": priority,
            }
        )

        save_tasks()

        flash("Task " + task_id + " created.", "success")

        return redirect(url_for("task.view_tasks"))

    return render_template(
        "create_task.html", statuses=STATUSES, priorities=PRIORITIES, form=None
    )


@task_bp.route("/task/<task_id>")
def task_details(task_id):

    task = find_task(task_id)

    if task is None:
        flash("Task ID " + task_id + " does not exist.", "error")
        return redirect(url_for("task.view_tasks"))

    return render_template("task_details.html", task=task)


@task_bp.route("/update-task/<task_id>", methods=["GET", "POST"])
def update_task(task_id):

    task = find_task(task_id)

    if task is None:
        flash("Task ID " + task_id + " does not exist.", "error")
        return redirect(url_for("task.view_tasks"))

    if request.method == "POST":

        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        priority = request.form.get("priority", "Medium").strip()

        if not title or not description:
            flash("Title and description cannot be empty.", "error")

            return render_template("update_task.html", task=task, priorities=PRIORITIES)

        if priority not in PRIORITIES:
            priority = "Medium"

        task["title"] = title
        task["description"] = description
        task["priority"] = priority

        save_tasks()

        flash("Task " + task["task_id"] + " updated.", "success")

        return redirect(url_for("task.view_tasks"))

    return render_template("update_task.html", task=task, priorities=PRIORITIES)


@task_bp.route("/search")
def search():

    keyword = request.args.get("keyword", "").strip()

    results = []
    searched = False

    if keyword:

        searched = True
        keyword = keyword.lower()

        for task in tasks:
            if (
                keyword in task["title"].lower()
                or keyword in task["description"].lower()
            ):
                results.append(task)

    return render_template(
        "search.html", keyword=keyword, results=results, searched=searched
    )


@task_bp.route("/status/<task_id>", methods=["GET", "POST"])
def change_status(task_id):

    task = find_task(task_id)

    if task is None:
        flash("Task ID " + task_id + " does not exist.", "error")
        return redirect(url_for("task.view_tasks"))

    if request.method == "POST":

        new_status = request.form.get("status", "").strip()

        if new_status not in STATUSES:
            flash("Please choose a valid status.", "error")

            return redirect(url_for("task.change_status", task_id=task["task_id"]))

        task["status"] = new_status

        save_tasks()

        flash("Task " + task["task_id"] + " is now " + new_status + ".", "success")

        return redirect(url_for("task.view_tasks"))

    return render_template("status.html", task=task, statuses=STATUSES)


@task_bp.route("/delete-task/<task_id>", methods=["POST"])
def delete_task(task_id):

    task = find_task(task_id)

    if task is None:
        flash("Task ID " + task_id + " does not exist.", "error")

    else:
        tasks.remove(task)

        save_tasks()

        flash("Task " + task["task_id"] + " deleted.", "success")

    return redirect(url_for("task.view_tasks"))
