from flask import Flask, render_template

app = Flask(__name__)

# 정적 파일 서빙 설정

app.static_folder = 'static'

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/login')
def login():

    return render_template('login.html')


if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)


