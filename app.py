from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
  return "hello world from neural automation WIP!!!"


app.run(port=4999,debug=True)