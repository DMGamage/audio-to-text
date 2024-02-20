import speech_recognition

recognizer = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
        continue
