from flask import Flask

app = Flask(__name__)

@app.route('/upload')
def upload_file():
    return {"messages": ["Content One Test", "Content Two Test", "Content Three Test", "Content Four Test", "Content Five Test",]}

if __name__ == '__main__':
    app.run(port=5000, debug=True)
