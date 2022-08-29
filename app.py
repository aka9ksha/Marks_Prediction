from flask import Flask, render_template, request
import joblib
import pickle

app = Flask(__name__)


model = pickle.load(open('Marks_Prediction/model.pkl','rb'))

@app.route('/')
def home():
   return render_template("index.html")

@app.route('/', methods=['POST'])
def main():
   if request.method == 'POST':
      num = float(request.form['number'])
      marks = model.predict([[num]])
   return render_template("index.html", marks = marks)


if __name__ == '__main__':
   app.run(debug = True)