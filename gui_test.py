import tkinter as tk
import subprocess
import time
from tkinter import PhotoImage
from PIL import Image, ImageTk


def run_enToEs_script():
    script_name = 'en_to_es.py'
    
    try:
        result = subprocess.run(['python', script_name], capture_output=True, text=True)
        time.sleep(0.1)
        if result.returncode == 0:
            output_text.config(text=f"Script executed successfully.\nOutput:\n{result.stdout}")
        else:
            output_text.config(text=f"Script execution failed.\nError:\n{result.stderr}")
    except Exception as e:
        output_text.config(text=f"An error occurred: {str(e)}")
    


def run_esToEn_script():
    script_name = 'es_to_en.py'
    
    try:
        result = subprocess.run(['python', script_name], capture_output=True, text=True)
        time.sleep(2)
        if result.returncode == 0:
            output_text.config(text=f"Script executed successfully.\nOutput:\n{result.stdout}")
        else:
            output_text.config(text=f"Script execution failed.\nError:\n{result.stderr}")
    except Exception as e:
        output_text.config(text=f"An error occurred: {str(e)}")





root = tk.Tk()
root.title("Speech Translator")
root.geometry("500x500")

image = Image.open("app_icon_copy.jpg")
image.thumbnail((125, 125))
tk_image = ImageTk.PhotoImage(image)


label = tk.Label(root, text="Welcome to My GUI App", image=tk_image)
label.pack()

button = tk.Button(root, text="Speak English", command=run_enToEs_script, width=15, height=3, font=("Helvetica", 16, "bold"))
button.pack()

button = tk.Button(root, text="Habla Espanol", command=run_esToEn_script, width=15, height=3,font=("Helvetica", 16, "bold"))
button.pack()

output_text = tk.Label(root, text="", font=("Helvetica", 18, "normal"))
output_text.pack()


root.mainloop()