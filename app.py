from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello my name is tasnim i love reading books and eating chips!"

if __name__ == '_main_':
    app.run()
