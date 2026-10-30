from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return dict(message="Hello, World!")

@app.route("/")
def status():
    return dict(status="ok")

@app.route("/health")
def health():
    return dict(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)