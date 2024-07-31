from flask import Flask, render_template, request, jsonify
import revisor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.form['code']
    errors, tokens, syntaxs = revisor.analyze_code(code)
    return jsonify({'errors': errors, 'tokens': tokens, 'syntaxs': syntaxs})

if __name__ == '__main__':
    app.run(debug=True)
