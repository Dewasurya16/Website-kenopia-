from flask import Flask, request, render_template
import predict as pr
import predict1 as p1
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/curhat')
def curhat():
    return render_template('Curhat.html')

@app.route('/predict', methods=['POST'])
def predicts1():
    if request.method == 'POST':
        # mengambil value POST method
        curhat = request.form['message']
        result = p1.predict1(curhat)
        input_text = request.form['message']
        prediction = pr.predict(input_text)
        return render_template('Curhat.html', result1=result,prediction_text=prediction)

if __name__ == "__main__":
    app.run(debug=True)