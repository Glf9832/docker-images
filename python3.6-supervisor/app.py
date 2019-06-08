from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>首页</h1>'

@app.route('/api')
def api():
    return '<h1>API测试</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
