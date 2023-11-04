import tkinter as tk
import subprocess
import time
# import threading


def run_script():
    # Replace 'your_script.py' with the name of your Python script to execute
    script_name = 'translate.py'
    # while True:
    try:
        result = subprocess.run(['python', script_name], capture_output=True, text=True)
        if result.returncode == 0:
            output_text.config(text=f"Script executed successfully.\nOutput:\n{result.stdout}")
        else:
            output_text.config(text=f"Script execution failed.\nError:\n{result.stderr}")
    except Exception as e:
        output_text.config(text=f"An error occurred: {str(e)}")


root = tk.Tk()
root.title("Speech Translator")
root.geometry("400x300")

label = tk.Label(root, text="Welcome to My GUI App")
label.pack()

# button = tk.Button(root, text="Translate Speech", command=run_script)
button = tk.Button(root, text="Start Continuous Execution", command=run_script)
button.pack()

output_text = tk.Label(root, text="")
output_text.pack()


root.mainloop()