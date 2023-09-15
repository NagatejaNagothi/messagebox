from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    form = """
    <form action="/submit" method="get">
        <input type="text" name="name">
        <input type="text" name="message">
        <input type="submit" value="Submit">
    </form>
    """
    return render_template("index.html", form=form)

@app.route("/submit", methods=["GET"])
def submit():
    name = request.args.get("name")
    message = request.args.get("message")

    return f"Your name is {name}.\nYour message is {message}."

if __name__ == "__main__":
    app.run(debug=True)
