from flask import Flask, request, render_template
from PhishDetector import ThreatDetector

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    subject = request.form['subject']
    body = request.form["body"]
    sub_file = 'subject_threat_words.txt'
    bod_file = 'body_threat_words.txt'
    detector = ThreatDetector(sub_file, bod_file)
    detector.detect_subject(subject)
    detector.detect_body(body)
    sub_threats, bod_threats = detector.return_threats()
    subject_threats = ','.join(sub_threats)
    body_threats = ','.join(bod_threats)
    return subject_threats, body_threats

if __name__ == "__main__":
    app.run(port=5000, debug=True)