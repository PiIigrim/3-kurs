import tkinter as tk
from tkinter import filedialog, ttk
import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk import pos_tag
from nltk.corpus import stopwords

# Перевод на русский
pos_translation = {
    'CC': 'союз',
    'CD': 'числительное',
    'DT': 'определитель',
    'EX': 'существительное-экзистенциальное',
    'FW': 'неизвестное иноязычное слово',
    'IN': 'предлог',
    'JJ': 'прилагательное',
    'JJR': 'прилагательное сравнительной степени',
    'JJS': 'прилагательное превосходной степени',
    'LS': 'маркер элементарного списка',
    'MD': 'модальный глагол',
    'NN': 'существительное',
    'NNS': 'существительное множественного числа',
    'NNP': 'имя собственное',
    'NNPS': 'имя собственное множественного числа',
    'PDT': 'предопределитель',
    'POS': 'притяжательный маркер',
    'PRP': 'личное местоимение',
    'PRP$': 'притяжательное местоимение',
    'RB': 'наречие',
    'RBR': 'наречие сравнительной степени',
    'RBS': 'наречие превосходной степени',
    'RP': 'частица',
    'SYM': 'символ',
    'TO': 'маркер к инфинитиву',
    'UH': 'междометие',
    'VB': 'глагол в базовой форме',
    'VBD': 'глагол в прошедшем времени',
    'VBG': 'глагол в настоящем времени',
    'VBN': 'глагол в прошедшем или причастном времени',
    'VBP': 'глагол в настоящем времени, единственное число',
    'VBZ': 'глагол в настоящем времени, 3 лицо, единственное число',
    'WDT': 'какой-то детерминатив',
    'WP': 'вопросительное местоимение',
    'WP$': 'вопросительное притяжательное местоимение',
    'WRB': 'вопросительное наречие'
}

class PDFAnalyzerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("KnowYourPDF")

        self.label = ttk.Label(master, text="KnowYourPDF", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.open_button = ttk.Button(master, text="Выбрать PDF файл", command=self.open_pdf)
        self.open_button.pack(pady=5)

        self.filename_label = ttk.Label(master, text="", font=("Helvetica", 10))
        self.filename_label.pack(pady=5)

        self.frame = ttk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.text_area = tk.Text(self.frame, wrap="word", width=60, height=20)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.text_area.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self.text_area.config(yscrollcommand=self.scrollbar.set)

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.filename_label.config(text=f"Выбранный файл: {file_path}")
            self.read_pdf(file_path)

    def read_pdf(self, file_path):
        with open(file_path, "rb") as f:
            pdf_reader = PyPDF2.PdfReader(f)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
        self.analyze_text(text)

    def analyze_text(self, text):
        words = word_tokenize(text)
        stop_words = set(stopwords.words("english"))
        filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
        fdist = FreqDist(filtered_words)
        sorted_fdist = sorted(fdist.items())
        self.text_area.delete(1.0, tk.END)
        for word, freq in sorted_fdist:
            tagged_word = pos_tag([word])[0]
            self.text_area.insert(tk.END, f"{freq}: {word} - {tagged_word[1]}\n")

def main():
    root = tk.Tk()
    app = PDFAnalyzerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()