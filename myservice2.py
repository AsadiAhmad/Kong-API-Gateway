from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hi, I'm service 2"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.2', port=8080)
