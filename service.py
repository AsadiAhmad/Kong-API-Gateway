from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print("Received a request!")
    return 'This is rate limiting Plugin from KONG !'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

