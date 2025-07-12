# Handles speech-to-text conversion

import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        # Reduce noise
        r.adjust_for_ambient_noise(source, duration=0.8)
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=4)
            text = r.recognize_google(audio)
            print(f"Me: {text}")
            return text
        except sr.WaitTimeoutError:
            print(" No speech detected.")
        except sr.UnknownValueError:
            print(" Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print(f" Network error: {e}")
        except Exception as e:
            print(f" Error: {e}")
        return ""
