import time
import random
import tkinter as tk
from tkinter import messagebox, simpledialog

def generate_random_text(word_count):
    words = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog", 
             "a", "an", "in", "on", "at", "to", "for", "with", "by", "from", 
             "up", "down", "is", "are", "was", "were", "be", "been", "being", 
             "have", "has", "had", "do", "does", "did", "will", "would", 
             "shall", "should", "may", "might", "must", "can", "could"]
    return " ".join(random.choices(words, k=word_count))

def calculate_wpm(typed_text, elapsed_time):
    words = typed_text.split()
    return len(words) / (elapsed_time / 60)

def calculate_accuracy(original_text, typed_text):
    original_words = original_text.split()
    typed_words = typed_text.split()
    correct_words = sum(a == b for a, b in zip(original_words, typed_words))
    return (correct_words / len(original_words)) * 100

def start_typing_test():
    global test_text, start_time
    test_text = generate_random_text(50)
    text_display.config(state=tk.NORMAL)
    text_display.delete(1.0, tk.END)
    text_display.insert(tk.END, test_text)
    text_display.config(state=tk.DISABLED)
    
    entry.delete(0, tk.END)
    entry.focus()
    start_time = time.time()
    root.after(10000, end_typing_test)

def end_typing_test():
    typed_text = entry.get()
    elapsed_time = time.time() - start_time
    wpm = calculate_wpm(typed_text, elapsed_time)
    accuracy = calculate_accuracy(test_text, typed_text)

    messagebox.showinfo("Results", f"Your typing speed: {wpm:.2f} WPM\nAccuracy: {accuracy:.2f}%")

    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Typing Test")

text_display = tk.Text(root, height=10, width=50, state=tk.DISABLED)
entry = tk.Entry(root, width=50)
start_button = tk.Button(root, text="Start Typing Test", command=start_typing_test)

text_display.pack(pady=20)
entry.pack(pady=10)
start_button.pack(pady=10)

root.mainloop()
