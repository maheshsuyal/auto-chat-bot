import pyautogui
import time
import pyperclip
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env")

client = genai.Client(api_key=api_key)

inactive_count = 0
max_inactive_cycles = 10


def should_auto_reply(copied_text, your_name="Mahesh"):
    global inactive_count

    lines = copied_text.strip().splitlines()[-1]

    if your_name in lines:
        inactive_count += 1
        return False

    return True


print("Starting in 3 seconds...")
time.sleep(3)

pyautogui.click(1349, 1050)

print("Clicked on the icon.")

time.sleep(2)

while True:

    pyautogui.moveTo(698, 134, duration=0.5)
    pyautogui.mouseDown()
    pyautogui.moveTo(724, 951, duration=1)
    pyautogui.mouseUp()

    print("Selected the text.")

    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)

    pyautogui.click(698, 134)

    chat_history = pyperclip.paste()

    print("Copied Text:", chat_history)

    if should_auto_reply(chat_history, your_name="Mahesh"):

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=f"""Chat conversation:
{chat_history}

you are a person named Mahesh who speaks Hindi as well as English. He is from India and is a coder. Analyze the chat history and respond like Mahesh. Give the best reply according to the situation and emotion. Do not give explanation or multiple replies. Give only one reply. Use emoji when appropriate. You can use casual language and slang if it fits the conversation. Only write the reply:"""
        )

        reply = response.text.strip()

        print("Auto Reply:\n", reply)

        pyperclip.copy(reply)

        time.sleep(2)

        pyautogui.click(x=802, y=975)

        time.sleep(1)

        pyautogui.hotkey("ctrl", "v")

        time.sleep(0.5)

        pyautogui.press("enter")

    if inactive_count >= max_inactive_cycles:
        break