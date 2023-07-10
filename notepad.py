from tkinter import * 
from tkinter import filedialog
#lets define all functions here
def open_file():
    filepath = filedialog.askopenfilename(initialdir="C:/Users/LuCiFeRsTaR/Desktop/",
                                          title='open file',
                                          filetypes=(("textfile","*.txt"),("all files","**")))
    print(filepath)
    file = open(filepath,'r')
    print(file.read())
    file.close()



def save_file():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[("Text File",".txt"),
                                               ("HTML File",".html"),
                                               ("All file",".*"),]) 
    if file is None:
        return
    filetext = str(text.get(1.0,END)) #we can also take user input
    file.write(filetext)
    file.close()
def copy():
    selected_text = text.get(SEL_FIRST, SEL_LAST)
    old_window.clipboard_clear()
    old_window.clipboard_append(selected_text)

def cut():
    selected_text = text.get(SEL_FIRST, SEL_LAST)
    old_window.clipboard_clear()
    old_window.clipboard_append(selected_text)
    text.delete(SEL_FIRST, SEL_LAST)

def paste():
    texts = old_window.clipboard_get()
    text.insert(INSERT, texts)

def about():
    aboutwindow = Tk()
    def exit():
        aboutwindow.destroy()
    aboutwindow.title('Welcome to RockStar NotePad')
    abouttext = 'Hello everyone this notepad is created by RoyalRockStar(sumit) using tkinter and some built-in function of tkinter ."\n" We warm welcome our user for using this notepad ,"\n" More projects and update will be coming soon and shortly there will be a website for everything like this  '
    aboutlabel = Label(aboutwindow,
                        text=abouttext,
                        font=('Arial',15,),
                        fg='#00ff00',
                        bg='black',
                        relief=RAISED,
                        bd=10,
                        padx=20,
                        pady=20,
                        compound = 'top')
    aboutlabel.pack()
    aboutbutton = Button(aboutwindow,text='Thank You',font=('Arial',15),command=exit,width=100,height=1)
    aboutbutton.pack()
    aboutbutton.config(bg='darkblue',fg='white')
    
def help():
    def helpexit():
        helpwindow.destroy()
    helpwindow = Tk()
    helptext = 'This will be updated soon'
    helplabel =Label(helpwindow,
                     text=helptext,
                        font=('Arial',15,),
                        fg='#00ff00',
                        bg='black',
                        relief=RAISED,
                        bd=10,
                        padx=20,
                        pady=20,
                        compound = 'top')
    helplabel.pack()
    helpbutton = Button(helpwindow,text='Thank You',font=('Arial',15),command=helpexit,width=100,height=1)
    helpbutton.pack()
    helpbutton.config(bg='red',fg='white')
def font():
    def fontexit():
        fontwindow.destroy()
    fontwindow = Tk()
    fonttext = 'This will be updated soon'
    fontlabel =Label(fontwindow,
                     text=fonttext,
                        font=('Arial',15,),
                        fg='#00ff00',
                        bg='black',
                        relief=RAISED,
                        bd=10,
                        padx=20,
                        pady=20,
                        compound = 'top')
    fontlabel.pack()
    fontbutton = Button(fontwindow,text='Thank You',font=('Arial',15),command=fontexit,width=100,height=1)
    fontbutton.pack()
    fontbutton.config(bg='black',fg='white')
    

#creating a new window with same fuynctionality like old_window here

def newwindow():
    def savefile():
        new_file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[("Text File",".txt"),
                                               ("HTML File",".html"),
                                               ("All file",".*"),]) 
        if new_file is None:
            return
        new_filetext = str(netext.get(1.0,END)) #we can also take user input
        new_file.write(new_filetext)
        new_file.close()
    def new_copy():
        selected_texts = netext.get(SEL_FIRST, SEL_LAST)
        newwindow.clipboard_clear()
        newwindow.clipboard_append(selected_texts)

    def new_cut():
        selected_texts = netext.get(SEL_FIRST, SEL_LAST)
        newwindow.clipboard_clear()
        newwindow.clipboard_append(selected_texts)
        netext.delete(SEL_FIRST, SEL_LAST)

    def new_paste():
        textss = newwindow.clipboard_get()
        netext.insert(INSERT, textss)
#new window starts from here

    newwindow = Tk()
    newwindow.geometry("420x420")
    new_menubar = Menu(newwindow)
    newwindow.config(menu=new_menubar)
    new_filemenu = Menu(new_menubar,tearoff=0) 
    new_menubar.add_cascade(label="file", menu=new_filemenu) 
    new_filemenu.add_command(label="open",command=open_file)
    new_filemenu.add_command(label="save",command=savefile)
    new_filemenu.add_command(label="new_window",command=newwindow)
    new_filemenu.add_separator()
    new_filemenu.add_command(label="exit",command=quit)
    #its an newwindow edit bar
    new_editMenu = Menu(new_menubar,tearoff=0)
    new_menubar.add_cascade(label="edit", menu=new_editMenu)
    new_editMenu.add_command(label="cut",command=new_cut)
    new_editMenu.add_command(label="copy",command=new_copy)
    new_editMenu.add_command(label="paste",command=new_paste)

    netext = Text(newwindow,font=("Italic",30),bg='#bdfff6',fg='#F96167')
    netext.pack()

#its an old window made in starting of file 

old_window = Tk()
old_window.geometry('620x520')
old_window.title('RockStar_NotePad')
notepad_image = PhotoImage(file='logo.png')
old_window.iconphoto(True,notepad_image)
menubar = Menu(old_window)
old_window.config(menu=menubar)
old_filemenu = Menu(menubar,tearoff=0) 
menubar.add_cascade(label="File", menu=old_filemenu) 
old_filemenu.add_command(label="Open",command=open_file)
old_filemenu.add_command(label="Save",command=save_file)
old_filemenu.add_command(label="New_window",command=newwindow)
old_filemenu.add_separator()
old_filemenu.add_command(label="Exit=>",command=quit)

#creating another dropdown for edit and its function

old_editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit", menu=old_editMenu)
old_editMenu.add_command(label="Cut",command=cut)
old_editMenu.add_command(label="Copy",command=copy)
old_editMenu.add_command(label="Paste",command=paste)

#lets create a help dropdown now
old_helpMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help?", menu=old_helpMenu)
old_helpMenu.add_command(label="Help",command=help)
old_helpMenu.add_command(label="Font",command=font)
old_helpMenu.add_command(label="About",command=about)

text = Text(old_window,font=("Italic",30),bg='#FFF748',fg='#080A52')
text.pack()
old_window.mainloop()