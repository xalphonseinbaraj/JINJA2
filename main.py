from flask import Flask

app =Flask(__name__)

@app.route('/')
def welcome():
    return 'this is flask file example111'


if __name__ =="__main__":
    app.run(debug=True)