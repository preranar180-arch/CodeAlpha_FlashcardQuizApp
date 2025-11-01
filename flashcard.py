import tkinter as tk
from tkinter import messagebox, simpledialog

class FlashcardApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Flashcard Quiz App")
        self.root.geometry("400x400")
        self.root.config(bg="#f2f2f2")

        # Flashcards list
        self.flashcards = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
        ]
        self.current_index = 0
        self.show_answer = False

        # Widgets
        self.question_label = tk.Label(
            root, text="", font=("Arial", 16, "bold"), wraplength=350, bg="#f2f2f2"
        )
        self.question_label.pack(pady=40)

        self.toggle_button = tk.Button(
            root, text="Show Answer", command=self.toggle_answer, width=15, bg="#4CAF50", fg="white"
        )
        self.toggle_button.pack(pady=5)

        nav_frame = tk.Frame(root, bg="#f2f2f2")
        nav_frame.pack(pady=10)

        tk.Button(nav_frame, text="Previous", command=self.prev_card, width=10).grid(row=0, column=0, padx=5)
        tk.Button(nav_frame, text="Next", command=self.next_card, width=10).grid(row=0, column=1, padx=5)

        edit_frame = tk.Frame(root, bg="#f2f2f2")
        edit_frame.pack(pady=10)

        tk.Button(edit_frame, text="Add", command=self.add_card, width=10, bg="#2196F3", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(edit_frame, text="Edit", command=self.edit_card, width=10, bg="#FFC107").grid(row=0, column=1, padx=5)
        tk.Button(edit_frame, text="Delete", command=self.delete_card, width=10, bg="#F44336", fg="white").grid(row=0, column=2, padx=5)

        self.update_card()

    def update_card(self):
        """Update the displayed flashcard"""
        if not self.flashcards:
            self.question_label.config(text="No flashcards available. Please add one!")
            self.toggle_button.config(state=tk.DISABLED)
            return
        self.toggle_button.config(state=tk.NORMAL)
        text = (
            self.flashcards[self.current_index]["answer"]
            if self.show_answer
            else self.flashcards[self.current_index]["question"]
        )
        self.question_label.config(text=text)
        self.toggle_button.config(text="Hide Answer" if self.show_answer else "Show Answer")

    def toggle_answer(self):
        """Toggle between question and answer"""
        self.show_answer = not self.show_answer
        self.update_card()

    def next_card(self):
        """Go to next card"""
        if self.flashcards:
            self.current_index = (self.current_index + 1) % len(self.flashcards)
            self.show_answer = False
            self.update_card()

    def prev_card(self):
        """Go to previous card"""
        if self.flashcards:
            self.current_index = (self.current_index - 1) % len(self.flashcards)
            self.show_answer = False
            self.update_card()

    def add_card(self):
        """Add a new flashcard"""
        question = simpledialog.askstring("Add Flashcard", "Enter question:")
        answer = simpledialog.askstring("Add Flashcard", "Enter answer:")
        if question and answer:
            self.flashcards.append({"question": question, "answer": answer})
            self.current_index = len(self.flashcards) - 1
            self.show_answer = False
            self.update_card()

    def edit_card(self):
        """Edit current flashcard"""
        if not self.flashcards:
            messagebox.showinfo("Info", "No flashcards to edit.")
            return
        current = self.flashcards[self.current_index]
        question = simpledialog.askstring("Edit Flashcard", "Edit question:", initialvalue=current["question"])
        answer = simpledialog.askstring("Edit Flashcard", "Edit answer:", initialvalue=current["answer"])
        if question and answer:
            self.flashcards[self.current_index] = {"question": question, "answer": answer}
            self.update_card()

    def delete_card(self):
        """Delete current flashcard"""
        if not self.flashcards:
            messagebox.showinfo("Info", "No flashcards to delete.")
            return
        del self.flashcards[self.current_index]
        self.current_index = 0
        self.show_answer = False
        self.update_card()

if __name__ == "__main__":
    window = tk.Tk()
    app = FlashcardApp(window)
    window.mainloop()
