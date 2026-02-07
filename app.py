from flask import Flask, render_template, request, jsonify
from predictor import predict_placement

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    cgpa = float(data["cgpa"])
    skills = data["skills"]

    result = predict_placement(cgpa, len(skills))
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)




