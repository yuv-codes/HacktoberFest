import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.expression = ""

        # Create the display frame
        self.display_frame = tk.Frame(self.root, bg="black")
        self.display_frame.pack(expand=True, fill="both")

        # Entry widget to display the result
        self.input_text = tk.StringVar()
        self.input_field = tk.Entry(self.display_frame, textvariable=self.input_text, font=('Arial', 28), bg="black", fg="white", borderwidth=0, justify="right")
        self.input_field.pack(expand=True, fill="both", ipadx=8, ipady=20)

        # Create the buttons frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(expand=True, fill="both")

        # Button layout
        self.create_buttons()

    def create_buttons(self):
        # Define button text and their respective positions
        buttons = [
            ('C', 1, 0), ('⌫', 1, 1), ('%', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0, 2), ('.', 5, 2), ('=', 5, 3)
        ]

        for (text, row, col, *span) in buttons:
            button = tk.Button(self.buttons_frame, text=text, font=('Arial', 18), bg="#4D4D4D", fg="white", 
                               activebackground="#666", activeforeground="white", 
                               width=5, height=2, borderwidth=0, 
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=(span[0] if span else 1), sticky="nsew", padx=5, pady=5)

        # Configure row/column weights so buttons resize with the window
        for i in range(6):
            self.buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        """Handle button click events."""
        if char == "C":
            self.expression = ""
        elif char == "⌫":  # Backspace functionality
            self.expression = self.expression[:-1]
        elif char == "=":
            self.calculate_result()
        else:
            self.expression += str(char)

        self.input_text.set(self.expression)

    def calculate_result(self):
        """Calculate the expression entered by the user."""
        try:
            result = str(eval(self.expression))
            self.expression = result
        except Exception as e:
            self.expression = "Error"

        self.input_text.set(self.expression)


# Main loop to run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
