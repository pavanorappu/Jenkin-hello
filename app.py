from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>CI/CD Project</title>
        </head>
        <body style="text-align:center; font-family:Arial; margin-top:100px;">
            <h1>🚀 Welcome!</h1>
            <h2>This is a CI/CD Pipeline Project</h2>
            <p>Built using Jenkins + Docker + AWS EC2</p>
            <p><b>Every GitHub push automatically deploys this app 🎯</b></p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
