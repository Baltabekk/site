from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Добро пожаловать на мой сайт!'

if __name__ == '__main__':
    app.run()
