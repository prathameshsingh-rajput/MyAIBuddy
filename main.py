from speech_input import listen
from response_engine import get_response
from text_to_speech import speak
import sys

def run_assistant():
    try:
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

    except KeyboardInterrupt:
        print("\nBuddy: Goodbye!")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_assistant()
