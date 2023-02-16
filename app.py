from flask import Flask, render_template, request, redirect, url_for
from waitress import serve

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', result=output)

@app.route('/output', methods=['POST', 'GET'])
def output():

    if request.method == "GET":
        return redirect(url_for("index"))

    text = request.form['text']
    
    includespace = request.form.get('spaces')
    
    if range(len(text)) > 1000:
        return render_template('output.html', output="Maximum length is 1000 characters to prevent abuse.")
    elif range(len(text)) <= 1000:
        pass

    if text:
        text = text.upper()
    if text == "":
        output = "Please enter a text to translate"
    morsecode = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "'": ".----.",
        "!": "-.-.--",
        "/": "-..-.",
        "(": "-.--.",
        ")": "-.--.-",
        "&": ".-...",
        ":": "---...",
        ";": "-.-.-.",
        "=": "-...-",
        "+": ".-.-.",
        "-": "-....-",
        "_": "..--.-",
        '"': ".-..-.",
        "$": "...-..-",
        "@": ".--.-.",
        " ": "/"
    }

    output = []
    for i in range(len(text)):
        for j in range(len(text[i])):
            output.append(morsecode[text[i][j]])
    output = " ".join(output)
    if text == None:
        output = "None"
    
    if includespace != "1":
        output = output.replace("/", " ")
    elif includespace == "1":
        pass
    
    return render_template('output.html', output=output)

if __name__ == '__main__':

    serve(app, port=5000, host='0.0.0.0', threads=1)



