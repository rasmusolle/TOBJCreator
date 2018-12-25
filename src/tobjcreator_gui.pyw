from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tobjcreator as tobjcreator
import os

def create(*args):
	if not os.path.exists(source_tobj.get()):
		messagebox.showerror("Error","Source TOBJ file doesn't exist.")
	elif len(dds_path.get()) > 255:
		messagebox.showerror("Error","DDS path is too long.")
	elif len(dds_path.get()) == 0 or len(output_tobj.get()) == 0:
		messagebox.showerror("Error","Please fill in all input boxes.")
	else:
		tobjcreator.main(source_tobj.get(),dds_path.get(),output_tobj.get())

root = Tk()
root.title("TOBJ Creator " + tobjcreator.version + " GUI")
#root.iconbitmap('/home/administrator/Github/tobjcreator/src/icon.ico')
root.resizable(False, False)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

source_tobj = StringVar()
dds_path = StringVar()
output_tobj = StringVar()

ttk.Label(mainframe, text="Source TOBJ File:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="DDS Path:").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Output TOBJ File:").grid(column=1, row=3, sticky=W)

source_tobj_entry = ttk.Entry(mainframe, width=30, textvariable=source_tobj).grid(column=2, row=1, sticky=(W, E))
dds_path_entry = ttk.Entry(mainframe, width=30, textvariable=dds_path).grid(column=2, row=2, sticky=(W, E))
output_tobj_entry = ttk.Entry(mainframe, width=30, textvariable=output_tobj).grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Run", command=create).grid(column=2, row=4, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', create)
root.mainloop()
