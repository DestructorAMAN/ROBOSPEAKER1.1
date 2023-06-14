from win32com.client import Dispatch

if __name__ == '__main__':
    speak = Dispatch("SAPI.SpVoice").Speak
    speak("Welcome to Robo Speaker 1.1 Created by AMAN")
    speak("Enter what you want me to speak: ")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "quit":
            speak("Thanks for Using RoboSpeaker 1.1")
            print("Thanks for Using RoboSpeaker 1.1")
            print("Created by AMAN")
            break
        speak({x})
