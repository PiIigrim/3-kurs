#1
import tkinter as tk
from tkinter import simpledialog, messagebox

class TripleListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Задание 1")

        self.lists = [[1], [2], [3]]

        self.listboxes = []
        for i in range(3):
            listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10)
            listbox.grid(row=i, column=0, padx=10, pady=10)
            self.listboxes.append(listbox)
            listbox.bind('<ButtonRelease-1>', lambda event, i=i: self.set_selected_list(i))

        self.populate_lists()

        for i, listbox in enumerate(self.listboxes):
            listbox.bind('<Double-Button-1>', lambda event, i=i: self.move_item(event, i))

        self.add_button = tk.Button(root, text="Добавить", command=self.add_item_dialog)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.edit_button = tk.Button(root, text="Редактировать", command=self.edit_item_dialog)
        self.edit_button.grid(row=1, column=1, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Удалить", command=self.delete_item)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

        self.selected_list = None
        self.selected_index = None

    def populate_lists(self):
        for i, lst in enumerate(self.lists):
            self.listboxes[i].delete(0, tk.END)
            for item in lst:
                self.listboxes[i].insert(tk.END, item)

    def move_item(self, event, source_index):
        selected_index = self.listboxes[source_index].curselection()
        if selected_index:
            selected_index = selected_index[0]
            item = self.lists[source_index].pop(selected_index)
            destination_index = (source_index + 1) % 3
            self.lists[destination_index].append(item)
            self.populate_lists()

    def add_item_dialog(self):
        if self.selected_list is not None:
            item = simpledialog.askstring("Добавить элемент", "Введите элемент:")
            if item:
                self.lists[self.selected_list].append(item)
                self.populate_lists()
        else:
            messagebox.showerror("Ошибка", "Выберите список для добавления элемента.")

    def edit_item_dialog(self):
        if self.selected_list is not None and self.selected_index is not None:
            current_item = self.listboxes[self.selected_list].get(self.selected_index)
            new_item = simpledialog.askstring("Редактировать элемент", "Измените элемент:", initialvalue=current_item)
            if new_item:
                self.lists[self.selected_list][self.selected_index] = new_item
                self.populate_lists()

    def delete_item(self):
        if self.selected_list is not None and self.selected_index is not None:
            item = self.lists[self.selected_list].pop(self.selected_index)
            messagebox.showinfo("Удалено", f"Элемент '{item}' удален.")
            self.populate_lists()

    def set_selected_list(self, list_index):
        self.selected_list = list_index
        selected_index = self.listboxes[list_index].curselection()
        if selected_index:
            self.selected_index = selected_index[0]
        else:
            self.selected_index = None

if __name__ == "__main__":
    root = tk.Tk()
    app = TripleListApp(root)
    root.mainloop()