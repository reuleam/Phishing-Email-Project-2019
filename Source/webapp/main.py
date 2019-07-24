from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    text = request.form['text']
    return text

if __name__ == "__main__":
    app.run(port=5000, debug=True)