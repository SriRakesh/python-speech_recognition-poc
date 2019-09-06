import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak anything . . .")
    try:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print("---> {}".format(text))
    except:
        print("sorry, speak again")