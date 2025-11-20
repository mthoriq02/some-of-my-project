from customtkinter import *

class Kalkulator:
    def __init__(self, master):
        self.master = master
        master.title("Kalkulator Sederhana")
        master.geometry("220x320")
        
        self.after_equal = False
        self.screen = StringVar()
        self.screen_entry = CTkEntry(
            master, textvariable=self.screen, width=190,height=40, font=('Arial', 11)
            )
        self.screen_entry.grid(row=0, column=0, columnspan=25, padx=10, pady=10)

        self.every_button = [
            ('C', 1, 0), ('<-', 1, 1), ('%', 1, 2), ('+', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('/', 3, 3),
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('*', 4, 3),
            (',', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
        ]

        for but, rows, col in self.every_button:
            if but == 'C':
                CTkButton(
                    master, text=but, width=40, height=40, command=self.clear
                    ).grid(
                        row=rows, column=col, padx=(9, 5), pady=(5, 5)
                        )

            elif but =='<-':
                CTkButton(
                    master, text=but, width=40, height=40, command=self.remove
                    ).grid(
                        row=rows, column=col, padx=(9, 5), pady=(5, 5)
                        )

            elif but == '=':
                CTkButton(
                    master, text=but, width=40, height=40, command=self.sama_dengan
                    ).grid(
                        row=rows, column=col, padx=(9, 5), pady=(5, 5)
                        )

            else:
                CTkButton(
                    master, text=but, width=40, height=40, command=lambda t=but:self.press(t)
                    ).grid(
                        row=rows, column=col, padx=(9, 5), pady=(5, 5)
                        )

    def press(self, values):
        if self.after_equal:
            if values.isdigit():
                self.screen.set("")
                self.after_equal = False

            else:
                self.after_equal = False
                pass

        current = self.screen.get() + values
        self.screen.set(current)


    def remove(self):
        now = self.screen.get()
        hapus = now[:-1]
        self.screen.set(hapus)

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
