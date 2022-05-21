from flask import Flask, render_template, request

import pickle

# load the model
with open("./profit_prediction_model.pkl", "rb") as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route("/", methods=["GET"])

def index():
    return render_template("index.html")



@app.route("/predict", methods=["GET"])

def predict_profit():

    print(request.args)

    rnd = int(request.args.get("rnd"))
    administration = int(request.args.get("administration"))
    marketing = int(request.args.get("marketing"))
    state = int(request.args.get("state"))
    profits = model.predict([[rnd, administration, marketing, state]])
    return f"<h1>Profit of the company will be $ {profits[0]:0.2f}</h1>"


app.run(host = "localhost", port = 5000, debug = True)



