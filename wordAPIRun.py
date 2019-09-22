import flask
import json

from flask import Flask, request
from wordApi import WordPreprocess

preprocess_app = Flask(__name__)
preprocess_obj = WordPreprocess()

@preprocess_app.route('/home')
def test_api():
        return "API is working!!!"
    
@preprocess_app.route('topwords', methods=['POST'])
def top_words_api()
    text = json.loads(request.data.decode())['text']
    top_words = preprocess_obj.top_words(text)
    return str(top_words)

@preprocess_app.route('lastwords', methods=['POST'])
def last_words_api()
    text = json.loads(request.data.decode())['text']
    last_words = preprocess_obj.last_words(text)
    return str(last_words)

if __name__ == "__main__":
    preprocess_app.run(host='0.0.0.0', port=80, debug=True)
