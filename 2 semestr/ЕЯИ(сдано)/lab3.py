import re
import html
from collections import defaultdict
from Levenshtein import distance
import tkinter as tk
from tkinter import ttk, filedialog

def load_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def preprocess_text(text):
    cleaned_text = re.sub('<[^<]+?>', '', text)
    cleaned_text = html.unescape(cleaned_text)
    return cleaned_text

def find_similar_words(input_word, text, max_distance):
    similar_words = defaultdict(list)
    words = text.split()
    for word in words:
        dist = distance(input_word, word)
        if dist <= max_distance:
            similar_words[dist].append(word)
    return similar_words

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
    if file_path:
        label_file.config(text=file_path)

def search():
    input_word = entry_word.get()
    max_distance = int(entry_distance.get())
    html_file_path = label_file.cget("text")

    if not html_file_path:
        tk.messagebox.showerror("Ошибка", "Выберите HTML файл")
        return

    html_text = load_html_file(html_file_path)
    cleaned_text = preprocess_text(html_text)

    similar_words = find_similar_words(input_word, cleaned_text, max_distance)

    output_text.delete(1.0, tk.END)
    for dist in sorted(similar_words.keys()):
        output_text.insert(tk.END, f"Редакционное расстояние: {dist}\n")
        for word in similar_words[dist]:
            output_text.insert(tk.END, f"{word}\n")
        output_text.insert(tk.END, "\n")

root = tk.Tk()
root.title("Поиск слов, или чет такое, 3-я лаба крч")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

label_word = ttk.Label(frame, text="Введите слово:")
label_word.grid(row=0, column=0, sticky="w")

entry_word = ttk.Entry(frame, width=30)
entry_word.grid(row=0, column=1, padx=5, pady=5)

label_distance = ttk.Label(frame, text="Максимальное расстояние:")
label_distance.grid(row=1, column=0, sticky="w")

entry_distance = ttk.Entry(frame, width=10)
entry_distance.grid(row=1, column=1, padx=5, pady=5)

button_choose_file = ttk.Button(frame, text="Выбрать файл", command=choose_file)
button_choose_file.grid(row=2, column=0, columnspan=2, pady=5)

label_file = ttk.Label(frame, text="Выбранный файл: ")
label_file.grid(row=3, column=0, columnspan=2, sticky="w")

button_search = ttk.Button(frame, text="Поиск", command=search)
button_search.grid(row=4, column=0, columnspan=2, pady=10)

output_text = tk.Text(frame, width=50, height=20)
output_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
