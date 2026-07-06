import webbrowser
import tkinter as tk

def open_support():
    webbrowser.open(
        "https://github.com/tsddev016/MinePanel-GUI/blob/main/suport"
    )

app = tk.Tk()
app.title("SOS")
app.geometry("300x200")

tk.Button(app, text="🆘 Support", command=open_support).pack(pady=20)

app.mainloop()
