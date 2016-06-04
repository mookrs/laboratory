from flask import Flask, request, make_response, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return redirect('https://www.baidu.com')

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


if __name__ == '__main__':
    app.run(debug=True)
