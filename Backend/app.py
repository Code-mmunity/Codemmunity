from flask import Flask

app = Flask(__name__)

@app.route('/')

@app.route('./login.html')

def login():

  pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
