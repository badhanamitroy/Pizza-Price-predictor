from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained model once at startup
model = pickle.load(open('pizza_model.pkl', 'rb'))

def predict_price(size):
    prediction = model.predict([[size]])
    return round(prediction[0], 2)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    size = None
    if request.method == 'POST':
        size = float(request.form['size'])
        prediction = predict_price(size)
    return render_template('index.html', prediction=prediction, size=size)

if __name__ == '__main__':
    app.run(debug=True)
