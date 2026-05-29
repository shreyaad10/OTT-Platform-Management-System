import tkinter as tk

root=tk.Tk()

root.geometry("700x700")
root.title("My First GUI")
label1=tk.Label(root, text="OTT Platform Management System", font=('Times New Roman',24))
label1.pack(padx=20,pady=20)

root.mainloop()
