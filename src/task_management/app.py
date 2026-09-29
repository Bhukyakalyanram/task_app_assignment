from flask import Flask, render_template

from routes.main import main_bp
from routes.task import task_bp

app = Flask(__name__)

app.secret_key = "secret-key"

app.register_blueprint(main_bp)
app.register_blueprint(task_bp)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
