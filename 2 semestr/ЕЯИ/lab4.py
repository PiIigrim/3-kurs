import tkinter as tk
from tkinter import filedialog, messagebox
import spacy
from striprtf.striprtf import rtf_to_text

# Загрузка модели spaCy для русского языка
nlp = spacy.load("ru_core_news_sm")

# Словарь для перевода меток частей речи
POS_TRANSLATIONS = {
    'ADJ': 'прилагательное',
    'ADP': 'предлог',
    'ADV': 'наречие',
    'AUX': 'вспомогательный глагол',
    'CONJ': 'союз',
    'CCONJ': 'союз',
    'DET': 'детерминатор',
    'INTJ': 'междометие',
    'NOUN': 'существительное',
    'NUM': 'числительное',
    'PART': 'частица',
    'PRON': 'местоимение',
    'PROPN': 'имя собственное',
    'PUNCT': 'пунктуация',
    'SCONJ': 'подчинительный союз',
    'SYM': 'символ',
    'VERB': 'глагол',
    'X': 'другое',
    'SPACE': 'пробел'
}

# Словарь для перевода меток зависимостей
DEP_TRANSLATIONS = {
    'ROOT': 'корень',
    'acl': 'модификатор глагола',
    'acomp': 'прилагательное, стоящее в роли определения',
    'advcl': 'временной или условный субординатор',
    'advmod': 'наречие',
    'amod': 'определение, выраженное прилагательным',
    'appos': 'приложение',
    'aux': 'вспомогательный глагол',
    'case': 'падеж',
    'cc': 'координация',
    'ccomp': 'дополнение глагола',
    'clf': 'классификатор',
    'compound': 'сложное слово',
    'conj': 'соединитель',
    'cop': 'глагол-связка',
    'csubj': 'подчиненное предложение-подлежащее',
    'dep': 'неопределенная связь',
    'det': 'определитель',
    'discourse': 'дискурсивная частица',
    'dislocated': 'выдвижение',
    'expl': 'эксплетив',
    'fixed': 'неизменяемая часть словосочетания',
    'flat': 'плоскость',
    'goeswith': 'связь с другим словом',
    'iobj': 'индиректный объект',
    'list': 'список',
    'mark': 'маркер',
    'nmod': 'модификатор существительного',
    'nsubj': 'подлежащее',
    'nummod': 'числительное',
    'obj': 'объект',
    'obl': 'обстоятельство',
    'orphan': 'сирота',
    'parataxis': 'параграф',
    'punct': 'пунктуация',
    'reparandum': 'репарандум',
    'root': 'корень',
    'vocative': 'вокатив',
    'xcomp': 'второстепенное зависимое предложение'
}

def analyze_text(text):
    doc = nlp(text)
    structures = []
    for sent in doc.sents:
        structure = {
            'text': sent.text,
            'parts_of_speech': [(token.text, translate_pos(token.pos_)) for token in sent],
            'dependencies': [(token.text, translate_dep(token.dep_), token.head.text) for token in sent]
        }
        structures.append(structure)
    return structures

def extract_text_from_rtf(filename):
    try:
        with open(filename, 'rb') as file:
            rtf_content = file.read()
            return rtf_to_text(rtf_content.decode('utf-8'))
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось извлечь текст из файла: {e}")
        return None

def translate_pos(pos):
    return POS_TRANSLATIONS.get(pos, pos)

def translate_dep(dep):
    return DEP_TRANSLATIONS.get(dep, dep)

def open_file():
    filename = filedialog.askopenfilename(filetypes=[("RTF Files", "*.rtf")])
    if filename:
        text = extract_text_from_rtf(filename)
        if text:
            structures = analyze_text(text)
            if structures:
                result_text.delete(1.0, tk.END)
                for structure in structures:
                    result_text.insert(tk.END, f"Текст: {structure['text']}\n")
                    result_text.insert(tk.END, "Части речи:\n")
                    for token, pos in structure['parts_of_speech']:
                        result_text.insert(tk.END, f"{token}: {pos}\n")
                    result_text.insert(tk.END, "\nЗависимости:\n")
                    for token, dep, head in structure['dependencies']:
                        result_text.insert(tk.END, f"{token} --{dep}--> {head}\n")
                    result_text.insert(tk.END, "\n" + "="*50 + "\n")
                update_result_text_size()

def update_result_text_size():
    width = int(root.winfo_width() * 0.6)
    height = root.winfo_height()
    result_text.config(width=width, height=height)

root = tk.Tk()
root.title("СинТОКСИЧНЫЙ мастер")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

open_button = tk.Button(frame, text="Открыть файл", command=open_file)
open_button.pack(side=tk.LEFT)

result_text = tk.Text(frame, width=50, height=20)
result_text.pack(side=tk.RIGHT)

root.bind("<Configure>", lambda event: update_result_text_size())

root.mainloop()