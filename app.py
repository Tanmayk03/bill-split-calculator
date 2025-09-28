from flask import Flask, render_template, request
import os  # needed for dynamic port

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def tip_calculator():
    result = None
    if request.method == "POST":
        try:
            total_bill = float(request.form["total_bill"])
            tip_percentage = float(request.form["tip_percentage"])
            people = int(request.form["people"])

            bill_with_tip = total_bill + total_bill * tip_percentage / 100
            result = round(bill_with_tip / people, 2)
        except:
            result = "Invalid input!"
    return render_template("index.html", result=result)

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
