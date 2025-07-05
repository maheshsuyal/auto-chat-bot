import pyautogui
import time
import pyperclip
import google.generativeai as genai


genai.configure(api_key="AIzaSyA5OB3v_DaADvrGxMaxO3GvJsuJXt0iBGE")


inactive_count = 0  # Yeh count karega kitni baar dusre user ka message nahi aaya
max_inactive_cycles = 10  # Agar 5 baar tak dusre user ka message nahi aaya toh band karo

def should_auto_reply(copied_text, your_name="Mahesh"):
    global inactive_count
    # Split copied text into individual lines to check last string
    lines = copied_text.strip().split('/2025] ')[-1]
    
    if your_name in lines:
        inactive_count+=1
        return False
    return True
       


# Give user 3 seconds to switch to proper screen
print("Starting in 3 seconds...")
time.sleep(3)

# Step 1: Click the icon
pyautogui.click(1349, 1050)
print("Clicked on the icon.")
time.sleep(2)  # wait for app to open

while True:

    # Step 2: Select text by dragging
    pyautogui.moveTo(698, 134, duration=0.5)
    pyautogui.mouseDown()
    pyautogui.moveTo(724, 951, duration=1)
    pyautogui.mouseUp()
    print("Selected the text.")

    # Step 3: Copy to clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # wait to copy
    pyautogui.click(698,134)


    # Step 4: Get text from clipboard
    chat_history = pyperclip.paste()
    print("Copied Text:", chat_history)

    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")
    
    if should_auto_reply(chat_history, your_name="Mahesh"):
         # Generate response like Mahesh
        response = model.generate_content(
            f"Chat conversation:\n{chat_history}\n\n you are person named mahesh who speaks hindi as well as english. he is from india and is a coder. you analyze the chat history and respond like mahesh give the best repy of chat_history as possible according to required emotion do not give explanation and multiple reply just give single reply use emoji also and you can also give gali if someone give and only write reply :"
        )

        print("Auto Reply:\n", response.text)



        pyperclip.copy(response.text)


        # Thoda wait karo taaki window ready ho
        time.sleep(2)

        # Step 1: Move to coordinates and click
        pyautogui.click(x=802, y=975)

        # Step 2: Wait after click
        time.sleep(1)

        # Step 3: Paste clipboard content using Ctrl + V
        pyautogui.hotkey('ctrl', 'v')

        # Step 4: Wait before pressing enter
        time.sleep(0.5)

        # Step 5: Press Enter
        pyautogui.press('enter')
        
    if inactive_count>=max_inactive_cycles:
        break
     
    

