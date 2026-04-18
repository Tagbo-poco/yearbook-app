from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open("data.json") as f:
    data = json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        name = request.form.get("name", "").lower()
        grade = request.form.get("grade", "").lower()
        class_ = request.form.get("class", "").lower()

        for student in data:
            if (name in student["name"].lower() and
                grade in student["grade"].lower() and
                class_ in student["class"].lower()):
                results.append(student)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)