import os
import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

#Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    person_id = session["user_id"]

    # get all the stock that user has
    symbols = [i["symbol"] for i in db.execute(
        "SELECT * FROM transactions WHERE userid = ? GROUP BY symbol HAVING SUM(shares) != 0", 
        person_id)]
        
    # create an empty list in order to store information about transaction
    transaction_info = []

    # get all necessary info about stocks
    for symbol in symbols:
        info = []
        share = lookup(symbol)
        info.append(share["symbol"])
        info.append(share["name"])
        number_of_shares = db.execute(
            "SELECT sum(shares) FROM transactions WHERE userid = ? AND symbol = ?", 
            person_id, symbol)[0]["sum(shares)"]
        info.append(number_of_shares)
        info.append(usd(share["price"]))
        info.append(usd(number_of_shares * share["price"]))
        transaction_info.append(info)

    # get amount of the cash that user has and store it in a variable named cash
    cash = db.execute("SELECT * FROM users WHERE id = ?", person_id)[0]["cash"]
    total = 0

    # get total worth of shares
    for i in transaction_info:
        total+= i[2] * lookup(i[0])["price"]

    # get how much money user has by adding user's cash to total
    total += cash

    total = usd(total)
    cash = usd(cash)
    
    return render_template("index.html", transaction_info = transaction_info, cash = cash, total = total)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # get user's id
        person_id = session["user_id"]

        # get the symbol of the share user wants to buy and store it in a variable named symbol
        symbol = request.form.get("symbol").upper()

        # get info about share using lookup function
        share = lookup(symbol)

        # Ensure symbol was submitted
        if not symbol:
            return apology("missing symbol", 400)

        # Ensure user submitted a valid symbol
        if not share:
            return apology("Invalid symbol", 400)

        # Ensure amount of share user wants to buy was submitted
        if not request.form.get("shares"):
            return apology("missing shares", 400)

        if not request.form.get("shares").isnumeric():
            return apology("share must be numeric value")
        # get amount of the shares user wants to buy
        share_amount = int(request.form.get("shares"))

        # get user's cash
        cash = db.execute("SELECT * FROM users WHERE id = ?", person_id)[0]["cash"]

        # get how much a share user wants to buy costs
        share_cost = share["price"]

        # get how much user needs to pay
        total = share_amount * share_cost

        # if user cannot afford return apology
        if cash < total:
            return apology("can't afford", 400)

        # get current time using datetime
        time_now = str(datetime.datetime.now())
        time_now = time_now[:time_now.index(".")]

        #insert all transaction infos to the database
        db.execute("INSERT INTO transactions (userid, symbol, shares, time, price) VALUES(?, ?, ?, ?, ?)", 
        person_id, symbol, share_amount, time_now, share_cost)

        # update user's cash
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - total, person_id)

        # redirect user to main page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # get user's id
    person_id = session["user_id"]

    # get all transaction from database and store it in a list named transaction_data
    transaction_data = [data for data in db.execute("SELECT * FROM transactions WHERE userid = ?", person_id)]
    for data in transaction_data:
        data["price"] = usd(data["price"])

    # render history.html with given list
    return render_template("history.html", transaction_data = transaction_data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        share_info = lookup(symbol)

        # if user submitted a valid symbol render quoted.html with given data otherwise return apology
        if (share_info):
            return render_template(
                "quoted.html", 
                name = share_info["name"], cost = usd(share_info["price"]), symbol = share_info["symbol"]
                )
        return apology("Invalid symbol", 400)

    if request.method == "GET":
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        # error checking
        if not request.form.get("username"):
            return apology("Missing Username", 400)

        if len(db.execute("SELECT username FROM users WHERE username = ?", request.form.get("username"))) == 1:
            return apology("Username is not available", 400)

        if not request.form.get("password"):
            return apology("Missing password", 400)

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords don't match", 400)

        # if no errors, register user
        db.execute("INSERT INTO users (username, hash, cash) VALUES(?, ?, ?)", 
        request.form.get("username"), generate_password_hash(request.form.get("password")), 10000.00)

    return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # get user's id
    person_id = session["user_id"]

    # get all stocks that user currently has
    shares = [i["symbol"] for i in db.execute("SELECT * FROM transactions WHERE userid = ? GROUP BY symbol HAVING SUM(shares) != 0", person_id)]

    if request.method == "GET":
        return render_template("sell.html", shares = shares)

    if request.method == "POST":
        share = request.form.get("symbol")

        # error checking
        if not share in shares:
            return apology("missing symbol", 400)

        input_share_amount = int(request.form.get("shares"))

        if not input_share_amount:
            return apology("missing shares", 400)

        # get amount of shares
        total_share_amount = db.execute("SELECT SUM(shares) FROM transactions WHERE userid = ? AND symbol = ?", person_id, share)[0]["SUM(shares)"]

        # if user tries to sell more shares than he/she has, throw an error
        if input_share_amount > total_share_amount:
            return apology("too many shares", 400)

        time_now = str(datetime.datetime.now())
        time_now = time_now[:time_now.index(".")]

        # save info of this sale
        db.execute("INSERT INTO transactions (userid, symbol, shares, time, price) VALUES(?, ?, ?, ?, ?)", person_id, share, 0 - input_share_amount, time_now, lookup(share)["price"])
        total_price = lookup(share)["price"] * input_share_amount
        cash = db.execute("SELECT * FROM users WHERE id = ?", person_id)[0]["cash"]
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + total_price, person_id)

        return redirect("/")

@app.route("/options", methods=["GET", "POST"])
@login_required
def options():
    if request.method == "GET":
        return render_template("options.html")

    if request.method == "POST":
        person_id = session["user_id"]
        button_value = request.form["button"]

        # user wants to change username
        if button_value == "1":
            if not request.form.get("new username"):
                return apology("missing username", 403)

            if not request.form.get("same password"):
                return apology("missing password", 403)

            if request.form.get("new username") == db.execute("SELECT * FROM users WHERE id = ?  ", person_id)[0]["username"]:
                return apology("new username can not be same as old username", 403)

            if not check_password_hash(db.execute("SELECT * FROM users WHERE id = ?  ", person_id)[0]["hash"], request.form.get("same password")) :
                return apology("Invalid password", 403)

            if db.execute("SELECT count(username) FROM users WHERE username = ?", request.form.get("new username"))[0]["count(username)"] == 1:
                return apology("username taken", 403)

            db.execute("UPDATE users SET username = ? WHERE id = ?", request.form.get("new username"), person_id)

            return redirect("/")
        # user wants to change password
        if button_value == "2":
            #error checking
            if not request.form.get("password"):
                return apology("missing password", 403)

            if not request.form.get("new password"):
                return apology("missing password", 403)

            if request.form.get("new password") != request.form.get("new password confirmation"):
                return apology("passwords don't match")

            if check_password_hash(db.execute("SELECT * FROM users WHERE id = ?  ", person_id)[0]["hash"], request.form.get("new password")) :
                return apology("New password can not be same as current password", 403)

            if not check_password_hash(db.execute("SELECT * FROM users WHERE id = ?  ", person_id)[0]["hash"], request.form.get("password")) :
                return apology("Invalid password", 403)

            # genereate hash for new password and store it in database
            db.execute("UPDATE users SET hash = ? WHERE id = ?", generate_password_hash(request.form.get("new password")), person_id)
            # redirect user to main page
            return redirect("/")
        # user wants to add cash
        if button_value == "3":
            if not request.form.get("cash"):
                return apology("missing cash", 403)
            # get user's cash
            cash = db.execute("SELECT * FROM users WHERE id = ?", person_id)[0]["cash"]
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + int(request.form.get("cash")), person_id)

            return redirect("/")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
