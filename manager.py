import os
from tkinter import *

file = open('paths.txt', 'r+')
read = file.readlines()
modified = []
names = []
urls = []

# create root window
root = Tk()
root.title("shortcut manager")
root.geometry('450x250') #size of window (width x height)

for line in read:
    line = line.replace( "\\","/" )

    if line[-1] == '\n':
        modified.append(line[:-1])
    else:
        modified.append(line)

for line in modified:
    names.append(line.split("|", 1)[0])
    urls.append(line.split("|", 1)[1])

#ui functions
def url_open(url):
    print("opened url: " + url)
    os.startfile(url)

def btn2_clicked():
    print("Saved Shortcut: " + txt.get() + "|" + txt1.get())
    file.write("\n" + txt.get() + "|" + txt1.get())

def open_help():
    print("help")
    help = Tk()
    help.title("help")
    #help.geometry('350x200')
    helplbl = Label(help, text = "This is a simple shortcut manager.")
    helplbl.grid(column=0, row=0)
    helplbl1 = Label(help, text = "Add a name and a path/url to create a shortcut.")
    helplbl1.grid(column=0, row=1)
    helplbl = Label(help, text = "For the new shortcut to show up, restart the program.")
    helplbl.grid(column=0, row=2)
    helplbl = Label(help, text = "Click on the 'open' button to open the path/url.")
    helplbl.grid(column=0, row=3)

#ui
#shortcuts
count=0
while len(names) > count:
    lbl = Label(root, text = names[count])
    lbl.grid(column=0, row=count)

    btn = Button(root, text = "open" ,fg = "red", command=lambda url=urls[count]: url_open(url))
    btn.grid(column=1, row=count)

    count += 1

#row one
lbl = Label(root, text = "Add shortcut")
lbl.grid(column=2, row=1+count)

#row two
lbl = Label(root, text = "Name:")
lbl.grid(column=0, row=2+count)

txt = Entry(root, width=10)
txt.grid(column =1, row =2+count)

lbl1 = Label(root, text = "url/path:")
lbl1.grid(column=3, row=2+count)

txt1 = Entry(root, width=10)
txt1.grid(column =4, row =2+count)

btn1 = Button(root, text = "Add" , command=btn2_clicked)
btn1.grid(column=6, row=2+count)

#row three
btn2 = Button(root, text = "Help" , command=open_help)
btn2.grid(column=6, row=0)

#run ui
root.mainloop()

#close file at end
file.close()