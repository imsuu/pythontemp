from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('login.html')

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return render_template('success.html')
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()
