from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
  return "hello world from neural automation WIP!!!"

if __name__ == '__main__':
    app.run(debug=True)