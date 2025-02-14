from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("http://app2:5001/data")  # Calling App 2
    return f"Response from App 2: {response.text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
