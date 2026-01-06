from flask import Flask, render_template, request
from utility import checkPrime, findPrimes, count_digits, check_char

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prime", methods=["POST"])
def prime():
    n = int(request.form["number"])
    result = "Prime" if checkPrime(n) else "Not Prime"
    return render_template("index.html", prime_result=result)

@app.route("/digits", methods=["POST"])
def digits():
    n = int(request.form["number"])
    result = count_digits(n)
    return render_template("index.html", digit_result=result)

@app.route("/char", methods=["POST"])
def char():
    ch = request.form["char"]
    result = check_char(ch)
    return render_template("index.html", char_result=result)

if __name__ == "__main__":
    app.run(debug=True)
