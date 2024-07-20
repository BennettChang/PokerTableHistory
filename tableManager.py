import tkinter as tk

class NumberSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker Table History")
        self.root.geometry("600x200")  # Set window size to 600x200 pixels
        self.root.config(bg="#2c3e50")  # Set background color

        self.numbers = []

        # Entry widget
        self.entry = tk.Entry(root, font=('Georgia', 24), bg="#ecf0f1", fg="#2c3e50", relief="solid", borderwidth=2)
        self.entry.pack(pady=10, ipady=5, ipadx=5)
        self.entry.bind("<Return>", self.add_or_remove_number)  # Bind the Enter key to add_or_remove_number method

        # Result label
        self.result_label = tk.Label(root, text="", font=('Georgia', 18), bg="#2c3e50", fg="#ecf0f1")
        self.result_label.pack(pady=10)

    def add_or_remove_number(self, event=None):
        input_text = self.entry.get()
        self.entry.delete(0, tk.END)

        try:
            if input_text.startswith('-'):
                number = int(input_text[1:])
                if number in self.numbers:
                    self.numbers.remove(number)
            else:
                number = int(input_text)
                if number not in self.numbers:
                    self.numbers.append(number)
            self.sort_numbers()  # Automatically sort and display numbers after adding or removing
        except ValueError:
            pass  # Silently handle invalid input

    def sort_numbers(self):
        sorted_numbers = sorted(self.numbers)
        self.result_label.config(text=f"Tables: {sorted_numbers}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberSorterApp(root)
    root.mainloop()