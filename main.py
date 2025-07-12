from speech_input import listen
from response_engine import get_response
from text_to_speech import speak

def run_assistant():
    while True:
        user_input = listen()   #speech_input.py

        if not user_input.strip():
            continue

        if "exit" in user_input.lower() or "stop" in user_input.lower():
            speak("Goodbye!")
            break

        response = get_response(user_input)
        print("Buddy:", response, "\n")
        speak(response)


if __name__ == "__main__":
    run_assistant()
