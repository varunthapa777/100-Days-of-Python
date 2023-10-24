import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(height=100, width=300)
window.config(padx=35, pady=20)

# new_label["text"] = "Hemlo"
# new_label.config(text="Hemlo")

entry = tkinter.Entry()
entry.grid(column=1, row=0)


first_label = tkinter.Label(text="Miles")
first_label.grid(column=2, row=0)

second_label = tkinter.Label(text="is equal to")
second_label.grid(column=0, row=1)

result = tkinter.Label(text="0")
result.grid(column=1, row=1)

third_label = tkinter.Label(text="Km")
third_label.grid(column=2, row=1)


def handle_click():
    mile = float(entry.get())
    km = round(mile*1.609, 2)
    result.config(text=f"{km}")


button = tkinter.Button(text="calculate", command=handle_click)
button.grid(column=1, row=2)




window.mainloop()

