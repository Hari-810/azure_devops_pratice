from flask import Flask

app = Flask(__name__)

@app.route('/data')
def data():
    return "Hello from App 2!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
