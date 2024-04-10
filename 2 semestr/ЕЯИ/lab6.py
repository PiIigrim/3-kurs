import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

class ChatBotApp:
    def __init__(self, master):
        self.master = master
        master.title("Кулинарный Чатбот")

        self.label = tk.Label(master, text="Введите ваш вопрос на английском:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Отправить", command=self.submit)
        self.submit_button.pack()

        self.chat_text = scrolledtext.ScrolledText(master, height=10, width=50)
        self.chat_text.pack(expand=True, fill=tk.BOTH)

        self.chatbot = Chat(self.get_pairs(), reflections)

    def submit(self):
        user_input = self.entry.get()
        response = self.chatbot.respond(user_input)
        self.chat_text.insert(tk.END, "Вы: " + user_input + "\n")
        self.chat_text.insert(tk.END, "Чатбот: " + response + "\n\n")
        self.entry.delete(0, tk.END)

    def get_pairs(self):
        return [
            ["What can I cook for dinner?", ["You can try pasta carbonara or grilled chicken."]],
            ["How do I make pizza?", ["You'll need dough, tomato sauce, cheese, and your favorite toppings."]],
            ["What's a good recipe for pancakes?", ["Mix flour, milk, eggs, and a pinch of salt. Cook on a hot pan until golden brown."]],
            ["How do I bake cookies?", ["Preheat your oven, mix butter, sugar, flour, and chocolate chips. Bake until golden."]],
            ["I want to learn cooking.", ["That's great! You can start with simple recipes like salads or soups."]],
            ["Tell me about kitchen safety.", ["Always wash your hands before cooking, use separate cutting boards for meat and vegetables, and keep knives out of reach of children."]],
            ["What's your favorite dish?", ["I'm just a chatbot, so I don't eat, but I've heard that spaghetti bolognese is popular."]],
            ["How long does it take to boil an egg?", ["It depends on how you like your eggs. For a soft-boiled egg, about 4-5 minutes, for a hard-boiled egg, about 8-10 minutes."]],
            ["What's the difference between baking soda and baking powder?", ["Baking soda needs an acid to activate it, while baking powder already contains an acid and just needs a liquid to start the reaction."]],
            ["", ["I'm sorry, I don't understand. Could you please rephrase your question?"]],
        ]

def main():
    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
