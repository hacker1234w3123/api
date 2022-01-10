from flask import Flask,jsonify,request
from model import prediction
app = Flask(__name__)

@app.route("/alphabet_predict",methods = ["POST"])
def Predict():
    image = request.files.get("alphabet")
    predict = prediction(image)
    return jsonify ({'data':predict , "message":"the alphabet is sucessfully recognized"})

if __name__ == '__main__':
    app.run(debug = True)