from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    def index():
        user_agent = request.headers.get("User-Agent")
        return '<p>Your browser is %s</p>' %user_agent

@app.route('/user/<name>')
def user(name):
    return 'Hello %s' % name

if __name__ == '__main__':
    app.run()
