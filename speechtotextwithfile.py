import speech_recognition as sr

def recognize_speech_from_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Tüm ses dosyasını kaydet
        try:
            command = recognizer.recognize_google(audio_data)
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Sorry, can you repeat, I don't understand.")
            return ""
        except sr.RequestError as e:
            print("We can't reach Google speech services; {0}".format(e))
            return ""

def main():
    file_path = input("Enter the path to the audio file: ")
    command = recognize_speech_from_audio(file_path).lower()
    if command:  # Tanınan metin varsa
        if "hello" in command:
            print("Hi!")
        elif "your name" in command:
            print("I'm venuux, your assistant.")
        elif "exit" in command:
            print("Goodbye!")

    else:
        print("No speech recognized.")

if __name__ == "__main__":
    main()
