from customtkinter import *

class Kalkulator:
    def __init__(self, master):
        self.master = master
        master.title("Kalkulator Sederhana")
        master.geometry("220x320")

        # ====================================
        # ATUR GRID ROOT AGAR BISA RESIZE
        # ====================================
        for i in range(6):          # baris 0 sampai 5
            master.rowconfigure(i, weight=1)

        for i in range(4):          # kolom 0 sampai 3
            master.columnconfigure(i, weight=1)

        # ====================================
        # ENTRY SCREEN (baris 0, kolom 0—3)
        # ====================================
        self.after_equal = False
        self.screen = StringVar()
        self.screen_entry = CTkEntry(
            master, textvariable=self.screen, font=('Arial', 15)
        )
        self.screen_entry.grid(row=0, column=0, columnspan=4,
                               sticky="nsew", padx=10, pady=10)

        # ====================================
        # BUTTONS
        # ====================================
        self.every_button = [
            ('C', 1, 0), ('<-', 1, 1), ('%', 1, 2), ('+', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('/', 3, 3),
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('*', 4, 3),
            (',', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
        ]

        for but, rows, col in self.every_button:

            # semua button dibuat tanpa width/height agar bisa auto-scale
            if but == 'C':
                CTkButton(master, text=but, command=self.clear)\
                    .grid(row=rows, column=col, sticky="nsew",
                          padx=5, pady=5)

            elif but == '<-':
                CTkButton(master, text=but, command=self.remove)\
                    .grid(row=rows, column=col, sticky="nsew",
                          padx=5, pady=5)

            elif but == '=':
                CTkButton(master, text=but, command=self.sama_dengan)\
                    .grid(row=rows, column=col, sticky="nsew",
                          padx=5, pady=5)

            else:
                CTkButton(master, text=but,
                          command=lambda t=but: self.press(t))\
                    .grid(row=rows, column=col, sticky="nsew",
                          padx=5, pady=5)

    # ====================================
    # FUNCTIONS
    # ====================================

    def press(self, values):
        if self.after_equal:
            if values.isdigit():
                self.screen.set("")
            self.after_equal = False

        current = self.screen.get() + values
        self.screen.set(current)

    def remove(self):
        now = self.screen.get()
        self.screen.set(now[:-1])

    def clear(self):
        self.screen.set("")

    def sama_dengan(self):
        try:
            result = eval(self.screen.get())
            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.screen.set(result)
            self.after_equal = True

        except:
            self.screen.set("Error")
            self.after_equal = True


root = CTk()
start = Kalkulator(root)
root.mainloop()
