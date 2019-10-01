from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')
    
@app.route('/rec/<query>')
def recommendation():
    sqft = request.args.get('sqft', '')
    return render_template('recommendation.html')