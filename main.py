from tkinter import  *
from tkinter import filedialog,messagebox
from PIL import Image, ImageTk

from stegano import lsb

win = Tk()
win.geometry('700x480')
win.config(bg='black')

#functions for button actions
def open_img():
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title='Select File Type',
                                           filetypes=(('PNG file','*.png'), ('JPG file','*.jpg'),
                                           ('All file','*.txt')))
    img = Image.open(open_file)
    img = ImageTk.PhotoImage(img)
    lf1.configure(image = img)
    lf1.image = img

def hide():
    global hide_msg
    password = code.get()
    if password == '1234':
        msg = text1.get(1.0, END)
        hide_msg = lsb.hide(open_file, msg)
        messagebox.showinfo('success', 'Your message is successfully hidden, please save your image')
    elif password == '':
        messagebox.showerror('Error', 'Please enter secret key')
    else:
        messagebox.showerror('error', 'Wrong secret key')
def save_img():
    hide_msg.save('Secret file.png')
    messagebox.showinfo('Saved','Your image is successfully saved')

def show():
    password = code.get()
    if password == '1234':
        show_msg = lsb.reveal(open_file)
        text1.delete(1.0,END)
        text1.insert(END, show_msg)
    elif password == '':
        messagebox.showerror('error','Please enter secret key to reveal message')
    else:
        messagebox.showerror('error','Please enter correct secret key')
        code.set('')

#logo setting
logo = PhotoImage(file='logoimg.png')
Label(win,image=logo,bd=0).place(x=180,y=0)
#heading
Label(win,text='Stegano', font='impaack 30 bold', bg='black', fg='red').place(x=260,y=12)

#frame1
f1 = Frame(win,width=250, height=220, bd = 5, bg='purple')
f1.place(x=50, y=100)
#label for frame 1
lf1 = Label(f1,bg='purple')
lf1.place(x=0, y=0)

#frame2
f2 = Frame(win,width=320,height=220,bd=5,bg='white')
f2.place(x=330, y= 100)
text1 = Text(f2,font='ariel 15 bold',wrap=WORD)
text1.place(x=0,y=0, width=320, height=210)
#Label for secret key
Label(win, text='Enter Secret Key', font=10, bg='black', fg='yellow').place(x=270,y=330)
#Entry widget for secret key
code = StringVar()
e = Entry(win,textvariable=code,bd=2, font='impact 10 bold', show='*')
e.place(x =245, y=360)
#Buttons
open_button = Button(win, text='Open Image', bg='blue', fg='white', font='ariel 12 bold', cursor='hand2', command=open_img)
open_button.place(x=60, y=417)

save_button = Button(win, text='Save Image', bg='green', fg='white', font='ariel 12 bold', cursor='hand2', command=save_img)
save_button.place(x=190, y=417)

hide_button = Button(win, text='Hide Data', bg='red', fg='white', font='ariel 12 bold', cursor='hand2', command=hide)
hide_button.place(x=380, y=417)

show_button = Button(win, text='Show Data', bg='orange', fg='white', font='ariel 12 bold', cursor='hand2', command=show)
show_button.place(x=510, y=417)
mainloop()
