from flask import Flask, render_template, url_for, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route('/home', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        extention = file.filename.split(".")[-1]
        if extention == 'wav':
            r = sr.Recognizer()
            with sr.AudioFile(file) as source:
                audio = r.record(source)
            try:
                #print("Content " + r.recognize_sphinx(audio))
                data = r.recognize_google(audio)
                return render_template('show.html', data=data)
            except sr.UnknownValueError:
                print("could not understand audio")
            except sr.RequestError as e:
                print("error; {0}".format(e))
        else:
            return render_template('index.html', alert = "Please upload '.wav' files only", isAlert = True)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)