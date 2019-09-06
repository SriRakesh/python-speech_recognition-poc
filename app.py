from flask import Flask, render_template, url_for, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route('/home', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        extention = file.filename.split(".")[-1]
        if extention == 'mp3' or extention == 'wav':
            r = sr.Recognizer()
            with sr.AudioFile(file) as source:
                audio = r.record(source)
            try:
                print("Content " + r.recognize_sphinx(audio))
            except sr.UnknownValueError:
                print("could not understand audio")
            except sr.RequestError as e:
                print("error; {0}".format(e))
        else:
            return "Please upload audio file"
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)