from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from scraper import *


# screen sizing
window = Tk()
window.title('Login')
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)


# sign-in function
def sign_in():
    username=user.get()
    pw=password.get()

    if username == 'admin' and pw == '1234':

        # ============ Scraper Window ==============
        screen = Tk()
        screen.title('Scraper')
        screen.geometry('925x500+300+200')
        screen.config(bg='white')
        screen.resizable(False,False)

        Label(screen, height=500, width=925, bg='white',fg='#fff', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)

        # Upload File Frame
        def UploadAction(event=None):
            global filename
            filename = filedialog.askopenfilename()
            return filename

        example = Frame(screen, width=350, height=200, bg='white')
        example.place(x=480, y=50)

        upload_header = Label(example, text='Example File', bg='white', fg='#C1272D', font=('Microsoft YaHei UI Light', 23, 'bold'))
        upload_header.place(relx=0.25, y=0)

        Frame(example, width=250, height=2, bg='#C1272D').place(x=50, y=38)

        Label(example, text='(Numbers represent the line number and', bg='white', font=('Microsoft YaHei UI Light', 12)).place(x=20, y=45)
        Label(example, text='should not be included in the file.)', bg='white', font=('Microsoft YaHei UI Light', 12)).place(x=40, y=70)

        # Example File for users to know how to properly format their input
        file = Frame(screen, height=175, width=350, highlightbackground='#C1272D', highlightthickness=1)
        file.place(x=480, y=160)

        line1 = Label(file, text='1.')
        line1.place(x=20, y=20)
        line2 = Label(file, text='2. https://homedepot.com/productname',  font=('Microsoft YaHei UI Light', 9))
        line2.place(x=20, y=40)
        line3 = Label(file, text='3. https://kirbyrisk.com/productname',  font=('Microsoft YaHei UI Light', 9))
        line3.place(x=20, y=60)
        line4 = Label(file, text='4. https://grainger.com/product',  font=('Microsoft YaHei UI Light', 9))
        line4.place(x=20, y=80)
        line5 = Label(file, text='5. https://kirbyrisk.com/product',  font=('Microsoft YaHei UI Light', 9))
        line5.place(x=20, y=100)
        line6 = Label(file, text='6. https://lowes.com/product_name',  font=('Microsoft YaHei UI Light', 9))
        line6.place(x=20, y=120)
        line7 = Label(file, text='7. https://kirbyrisk.com/product_name',  font=('Microsoft YaHei UI Light', 9))
        line7.place(x=20, y=140)

        # ========== Instructions Frame ===========

        instructions = Frame(screen, width=350, height=400, bg='white')
        instructions.place(x=50, y=50)

        instr_header = Label(instructions, text='Instructions', bg='white', fg='#C1272D', font=('Microsoft YaHei UI Light', 23, 'bold'))
        instr_header.place(relx=0.25, y=0)
        Frame(instructions, width=250, height=2, bg='#C1272D').place(x=50, y=38)

        # Step by step instructions for scraping file
        Label(instructions, text='1. Create a .txt file.', bg='white', font=('Microsoft YaHei UI Light', 12)).place(x=25, y=55)
        Label(instructions, text='2. Leave the first line of the document', bg='white', font=('Microsoft YaHei UI Light', 12)).place(x=25, y=85)
        Label(instructions, text='   blank.', bg='white', font=('Microsoft YaHei UI Light', 12)).place(x=28, y=115)
        Label(instructions, text='3. Include any competitor product links ', bg='white', font=('Microsoft YaHei UI Light', 12)).place(x=25, y=145)
        Label(instructions, text='   you would like to scrape. ', bg='white', font=('Microsoft YaHei UI Light', 12)).place(x=28, y=175)
        Label(instructions, text='4. Save your file, upload and export.', bg='white', font=('Microsoft YaHei UI Light', 12)).place(x=25, y=205)

        Label(instructions, text='File Name: ', bg='white', font=('Microsoft YaHei UI Light', 12)).place(x=40, y=300)
        sheet_name = Entry(instructions, width=20, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
        sheet_name.place(x=135, y=300)          # trying to get it so you can name the file, works but names the file '!frame3.!entry.xlsx'
        
        upload_btn = Button(instructions, width=15, pady=7, text='Upload', bg='#C1272D', fg='white', border=0, command=UploadAction)
        upload_btn.place(x=40, y=250) # upload button

        if upload_btn == ' ':
            messagebox.showerror('Invalid', 'You must upload a file first')
        else:
            export_btn = Button(instructions, width=15, pady=7, text='Export', bg='#C1272D', fg='white', border=0, command=lambda: main(filename, sheet_name.get()))
            export_btn.place(x=190, y=250)

        window.destroy() # destroys the login window

        screen.mainloop() # starts scraper window
    
    elif username != 'admin' and password != '1234':
        messagebox.showerror('Invalid', 'Invalid username and password')
    elif password != '1234':
        messagebox.showerror('Invalid', 'Invalid password')
    elif username != 'admin':
        messagebox.showerror('Invalid', 'Invalid username')

# ========= Login Page =============
img = PhotoImage(file='images/login.png')
Label(window, image=img, bg='white').place(relx=0.15, rely=0.2) # image file and placement

signin = Frame(window, width=350, height=350, bg='white') # sign-in header location
signin.place(x=480, y=70)

heading = Label(signin, text='Sign In', fg='#C1272D', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold')) # heading text and style
heading.place(x=100, y=5)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Username')

user = Entry(signin, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11)) # username entry box
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(signin, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter(e):
    password.delete(0, 'end')

def on_leave(e):
    name=password.get()
    if name=='':
        password.insert(0, 'Password')

password = Entry(signin, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11)) # password entry box
password.place(x=30, y=150)
password.insert(0, 'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)
Frame(signin, width=295, height=2, bg='black').place(x=25, y=177)

Button(signin, width=39, pady=7, text='Sign in', bg='#C1272D', fg='white', border=0, command=sign_in).place(x=35, y=204) # sign-in button

window.mainloop()

# ============ Writing to Excel ============

