import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

app = Flask(__name__)

#allows templates to auto reload
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///scores.db")

def low():
    print("Does not need a contingency plan")

def mid():
    print("consider a contingency plan")

def high():
    print("MANDATORY contingency plan")


@app.route("/", methods=["GET", "POST"])
def risks():
    if request.method == "POST":
        data1 = int(request.form["par1"])
        data2 = int(request.form["par2"])
        data3 = int(request.form["par3"])
        data4 = int(request.form["par4"])
        data5 = int(request.form["par5"])



        user_score1 = int(request.form["score1"])
        user_score2 = int(request.form["score2"])
        user_score3 = int(request.form["score3"])
        user_score4 = int(request.form["score4"])
        user_score5 = int(request.form["score5"])

        scale1 = int(data1 * user_score1)
        scale2 = int(data2 * user_score2)
        scale3 = int(data3 * user_score3)
        scale4 = int(data4 * user_score4)
        scale5 = int(data5 * user_score5)



        return render_template("done.html",  HC = scale1)

    else:
        return render_template("risk.html")






@app.route("/score", methods=["GET", "POST"])
def score():
    if request.method == "POST":
        data1 = int(request.form["par1"])
        data2 = int(request.form["par2"])
        data3 = int(request.form["par3"])
        data4 = int(request.form["par4"])
        data5 = int(request.form["par5"])



        user_score1 = int(request.form["score1"])
        user_score2 = int(request.form["score2"])
        user_score3 = int(request.form["score3"])
        user_score4 = int(request.form["score4"])
        user_score5 = int(request.form["score5"])

        scale1 = int(data1 * user_score1)
        scale2 = int(data2 * user_score2)
        scale3 = int(data3 * user_score3)
        scale4 = int(data4 * user_score4)
        scale5 = int(data5 * user_score5)

    return render_template ("calcrisk.html",  HC = scale1, HCa=scale2, HCb=scale3, HCc=scale4, HCd=scale5)