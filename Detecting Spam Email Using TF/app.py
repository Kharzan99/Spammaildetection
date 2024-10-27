from flask import Flask, request, render_template
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the saved model
model = joblib.load('model.pkl')

def detect_spam(email_text):
    # Make a prediction using the loaded classifier
    prediction = model.predict([email_text])
    return "This is a Spam Email!" if prediction == 1 else "This is not a Spam Email!"

@app.route('/', methods=['GET', 'POST'])
def index():
    email_text = ""
    result = None
    if request.method == 'POST':
        # Get email text from the form
        email_text = request.form['email_text']
        
        # Get the prediction
        result = detect_spam(email_text)
        
    return render_template('index.html', result=result, email_text=email_text)

if __name__ == '__main__':
    app.run(debug=True)

