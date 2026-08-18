import os

from flask import Flask, flash, render_template, request

from calculations import (
    analyze_triangular_number,
    calculate_circle_accuracy,
    generate_collatz_sequence,
)


app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "development-secret-key"
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/collatz", methods=["GET", "POST"])
def collatz():
    result = None
    starting_number = ""

    if request.method == "POST":
        starting_number = request.form.get(
            "starting_number",
            ""
        )

        try:
            result = generate_collatz_sequence(
                starting_number,
                max_steps=100
            )

        except ValueError as error:
            flash(str(error), "error")

    return render_template(
        "collatz.html",
        result=result,
        starting_number=starting_number
    )


@app.route("/circle", methods=["GET", "POST"])
def circle():
    result = None
    circumference = ""
    diameter = ""

    if request.method == "POST":
        circumference = request.form.get(
            "circumference",
            ""
        )

        diameter = request.form.get(
            "diameter",
            ""
        )

        try:
            result = calculate_circle_accuracy(
                circumference,
                diameter
            )

        except ValueError as error:
            flash(str(error), "error")

    return render_template(
        "circle.html",
        result=result,
        circumference=circumference,
        diameter=diameter
    )


@app.route("/triangular", methods=["GET", "POST"])
def triangular():
    result = None
    number = ""

    if request.method == "POST":
        number = request.form.get(
            "number",
            ""
        )

        try:
            result = analyze_triangular_number(number)

        except ValueError as error:
            flash(str(error), "error")

    return render_template(
        "triangular.html",
        result=result,
        number=number
    )


@app.errorhandler(404)
def page_not_found(error):
    return (
        render_template(
            "error.html",
            code="404",
            title="Page not found",
            message=(
                "The page you requested does not exist. "
                "Check the address or return to the homepage."
            )
        ),
        404
    )


@app.errorhandler(500)
def internal_server_error(error):
    return (
        render_template(
            "error.html",
            code="500",
            title="Something went wrong",
            message=(
                "The server could not complete the request. "
                "Please return to the homepage and try again."
            )
        ),
        500
    )


if __name__ == "__main__":
    app.run(debug=True)

