# Handles speech-to-text conversion

import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    r.energy_threshold = 4000  # Better for noisy environments
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("\nListening... (say 'stop' to exit)")

        try:
            # Reduce noise
            r.adjust_for_ambient_noise(source, duration=0.8)
            audio = r.listen(source, timeout=5, phrase_time_limit=8)

            text = r.recognize_google(audio).strip()
            print(f"Me: {text}")
            return text
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            print(" Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print(f" Network error: {e}")
        except Exception as e:
            print(f" Error: {e}")
        return ""
