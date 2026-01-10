from flask import Flask, render_template, request
from analyzer import analyze_password
from utils import hash_password
from cracker import dictionary_attack

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    cracked = None

    if request.method == "POST":
        password = request.form.get("password")

        result = analyze_password(password)
        pwd_hash = hash_password(password)
        cracked = dictionary_attack(pwd_hash, "wordlist.txt")

    return render_template("index.html", result=result, cracked=cracked)

if __name__ == "__main__":
    app.run()
