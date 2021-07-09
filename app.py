from flask import Flask,render_template,request,redirect,flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import RatesNotAvailableError

from helper import calculating_currency,currency_symbal

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh so secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.debug = True
toolbar = DebugToolbarExtension(app)

@app.route('/',methods=["POST","GET"])
def hello_world():
    convert_from = request.form.get("from",)
    convert_to = request.form.get("to")
    convert_amount = request.form.get("amount")

    if request.form:
        try:
            result = calculating_currency(convert_from,convert_to,convert_amount)
            symbal = currency_symbal(convert_to)
            return redirect(f"/result?currency-rate={result}&currency-symbal={symbal}")
        except ValueError:
            flash(f"Please entry a valid amount value: {convert_amount}")
            return redirect("/")
        
        except RatesNotAvailableError:
            flash(f"Please entry a valid currency value: {convert_from}")
            return redirect("/")
    
    return render_template("home.html")

@app.route("/result")
def the_result():
    the_result = request.args.get("currency-rate")
    the_symbal = request.args.get("currency-symbal")
    return render_template("result.html",result=the_result,symbal=the_symbal)