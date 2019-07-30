import os
from flask import Flask, request, render_template
from PhishDetector import ThreatDetector

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    subject_content = request.form['subject']
    body_content = request.form["body"]

    if (len(body_content)==0 or len(subject_content)==0):
        return render_template('index.html')
        
    detector = ThreatDetector()
    detector.detect_subject(subject_content)
    detector.detect_body(body_content)
    subject_threats, body_threats = detector.return_threats()
    subject_chance, body_chance = detector.return_stats()
    sub_threat_words = ""
    bod_threat_words = ""
    sub_rating = "Subject Threat Rating: " + str(round(subject_chance*100, 1)) + "%"
    bod_rating = "Body Threat Rating: " + str(round(body_chance*100, 1)) + "%"

    if len(subject_threats) == 0:
        sub_return = """There were no words in your subject line that we commonly found in phishing scams. 
                        This does not guarantee that it is not a phishing email. Please see the \"Resources\" 
                        for additional materials to assist in identifying threats"""
    else:
        sub_return = """There were one or more words found in your subject line that are commonly found in
                        phishing emails:"""
        sub_threat_words = ','.join([word + '\n'for word in subject_threats])
    if len(body_threats) == 0:
        bod_return = """There were no words in your email body that we commonly found in phishing scams. 
                        This does not guarantee that it is not a phishing email. Please see the \"Resources\" 
                        for additional materials to assist in identifying threats"""
    else:
        bod_return = """There were one or more words found in your email body that are commonly found in 
                        phishing emails:""" 
        bod_threat_words = ','.join([word + '\n'for word in body_threats])

    return render_template('output.html',sub_rating=sub_rating, sub_return=sub_return, sub_threat_words=sub_threat_words, bod_rating=bod_rating, bod_threat_words=bod_threat_words, bod_return=bod_return)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)