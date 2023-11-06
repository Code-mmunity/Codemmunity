from flask import Flask, render_template

app = Flask(__name__)

# 정적 파일 서빙 설정
app.static_folder = 'static'


@app.route('/')
def index():
    return render_template('index.html') # render_template( ) 함수를 사용하여 index.html 파일을 찾기 때문에, 웹 서버는 template 폴더 내에서 .html 파일을 찾을 것이며, .html 파일이 template 디렉터리 상에 없으면, jinja2 Error가 출력되기에 유의해야함.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
