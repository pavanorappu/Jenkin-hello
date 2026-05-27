from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Macha-Project Jenkins is working / sikro va da vera yadhuna project panla"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
