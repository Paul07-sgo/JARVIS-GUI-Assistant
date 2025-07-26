import tkinter as tk 
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def on_click():
    speak("Hello Paul, I AM JARVIS! , Your Personal AI Assistant.")

root = tk.Tk() 
root.title("JARVIS Assistant")
root.geometry("400x300")   

label = tk.Label(root,text = "Welcome to Jarvis!", font=("Helvetica", 16))
label.pack(pady=20)

speak_button = tk.Button(root, text="Speak", command = on_click, font=("Arial",15 ), bg = "blue" , fg ="white")
speak_button.pack(pady=20)

root.mainloop()