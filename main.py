from flask import Flask, render_template, jsonify
from Analyze import score as score_text
from base64 import b64decode as b64d
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/score/<b64>')
def score(b64):
    text = b64d(b64)
    avg, good, bad = score_text(b64)
    return jsonify({
        'score': avg,
        'good': good,
        'bad': bad
    })

app.run(debug=True)