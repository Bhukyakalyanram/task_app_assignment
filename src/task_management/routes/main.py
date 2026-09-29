from flask import Blueprint, render_template
from data import tasks

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    return render_template("index.html", total=len(tasks))
