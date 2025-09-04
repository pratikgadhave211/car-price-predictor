import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get user input (example: two features)
        feature1 = float(request.form["feature1"])
        feature2 = float(request.form["feature2"])
        
        prediction = model.predict([[feature1, feature2]])
        return render_template("index.html", result=prediction[0])
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
