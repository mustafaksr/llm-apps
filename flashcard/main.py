import os
from flask import Flask, render_template, request, jsonify
from llm_gen import *

app = Flask(__name__)

def create_flashcards(mInput, nInput):
    front_text = []
    back_text = []
    for i in range(mInput * nInput):
        front_text.append(f"front_{i}")
        back_text.append(f"back_{i}")

    return front_text, back_text

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/flashcards', methods=['POST'])
def create_flashcards_route():
    query = request.form['query']
    mInput = int(request.form['mInput'])
    nInput = int(request.form['nInput'])
    # front_text, back_text = create_flashcards(mInput, nInput)

    front_text, back_text = make_llm_cards(user_prompt=query,num=mInput*nInput)

    response = {
        'front': front_text,
        'back': back_text
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
