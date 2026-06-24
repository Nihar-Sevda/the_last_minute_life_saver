from flask import Flask, render_template, request
from gemini_service import generate_plan

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create-plan", methods=["POST"])
def create_plan():

    goal = request.form["goal"]
    deadline = request.form["deadline"]
    daily_hours = request.form["daily_hours"]

    ai_response = generate_plan(
        goal,
        deadline,
        daily_hours
    )

    return render_template(
        "result.html",
        response=ai_response
    )


if __name__ == "__main__":
    app.run(debug=True)
