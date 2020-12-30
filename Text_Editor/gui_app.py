import tkinter as tk
from tkinter import ttk,filedialog,Menu,messagebox

all_contents=dict()

def save_file(*args):
    file_path = filedialog.asksaveasfilename()

    try:
        filename = file_path.split("/")[-1]
        text_widget=get_text_widget()
        content = text_widget.get("1.0", "end-1c")

        with open(file_path, "w") as file:
            file.write(content)
    except (AttributeError, FileNotFoundError):
        print("Save operation cancelled")
        return

    notebook.tab("current", text=filename)     #current selected tab
    all_contents[str(text_widget)] = hash(content)


def get_text_widget():
    tab_widget = notebook.nametowidget(notebook.select())    #notebook.select()-->current tab name,tab_widget-->Frame
    text_widget = tab_widget.winfo_children()[0]             #text_widget-->Frame's children
    return text_widget

def open_file(*args):
    file_path=filedialog.askopenfilename()
    try:
        filename = file_path.split("/")[-1]
        with open(file_path, 'r') as file:
            content=file.read()
    except (AttributeError, FileNotFoundError):
        print("Open cancelled!")
        return

    create_file(content,filename)


def create_file(content='',title="untitled"):
    container = ttk.Frame(notebook)
    container.pack()

    text_area = tk.Text(container)
    text_area.insert("end",content)
    text_area.pack(side="left",fill="both", expand=True)
    notebook.add(container, text=title)                  #tab contains the frame, frame contains text and scrollbar
    scrollbar = ttk.Scrollbar(container,orient="vertical",command=text_area.yview)
    scrollbar.pack(side="right", fill="y")
    text_area["yscrollcommand"] = scrollbar.set

    all_contents[str(text_area)]=hash(content)

def check_for_changes(*args):   #check for changes when typing in the selected text area
    current = get_text_widget()
    content = current.get("1.0", "end-1c")
    name = notebook.tab("current")['text']

    if hash(content) != all_contents[str(current)]:
        if name[-1] != "*":
            notebook.tab("current", text=name + "*")
    elif name[-1] == "*":
        notebook.tab("current", text=name[:-1])

def delete_tab(event):
    try:
        current = get_text_widget()
        content = current.get("1.0", "end-1c")
        closetab.tk_popup(event.x_root, event.y_root)
        if hash(content) == all_contents[str(current)]:
            if len(notebook.tabs()) == 1:
                create_file()
            notebook.forget(notebook.select())
        else:
            answer=messagebox.askyesno("Warning!", "The file is not saved. Do you want to close tab?")
            if answer:
                if len(notebook.tabs()) == 1:
                    create_file()
                notebook.forget(notebook.select())
    finally:
        closetab.grab_release()

def exit():
    unsaved = False

    for tab in notebook.tabs():
        tab_widget = root.nametowidget(tab)
        text_widget = tab_widget.winfo_children()[0]
        content = text_widget.get("1.0", "end-1c")

        if hash(content) != all_contents[str(text_widget)]:
            unsaved = True
            break

    if unsaved:
        confirm = messagebox.askyesno("Warning!","You have unsaved changes. Are you sure you want to quit?")
        if not confirm:
            return

    root.destroy()


def about():
    messagebox.showinfo(title="Text Editor",message="")

root = tk.Tk()
root.title('')


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)  #menu inside application window
root.config(menu=menubar)

menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=create_file)
filemenu.add_command(label="Open", command=open_file,accelerator="Ctrl+p")
filemenu.add_command(label="Save", command=save_file,accelerator="Ctrl+l")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)

filemenu.bind_all("<Control-p>", open_file)
filemenu.bind_all("<Control-l>", save_file)
filemenu.bind_all("<KeyPress>", check_for_changes)

main = ttk.Frame(root)
main.pack(fill="both", expand=True,padx=(20,20),pady=(0,20))
tk.Label(main, text="Text Editor", bg="pink").pack(fill="x")

notebook = ttk.Notebook(main)
notebook.pack(expand=True, fill="both")

create_file()

closetab = Menu(root, tearoff = 0)
closetab.add_command(label ="Close")
notebook.bind("<Button-3>", delete_tab)


helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

root.mainloop()