from tkinter import *

#main application logic
def make_hash():
    import tkinter
    from tkinter import ttk
    from tkinter import messagebox
    import hashlib

    #main window
    window = Tk()
    window.title('Hash Algorithm Application')
    window.geometry("610x365")#main window size
    window.configure(background='black')#main window background color
    window.resizable(False, False)
    # input/output variables
    textentry = Entry(window, width=90, bg='white')
    textentry.place(x=3, y=230)
    entered_text = textentry.get()
    output = Text(window, width=75, height=6, wrap=WORD, background='white')
    output.place(x=3, y=260)
    output.delete(0.0, END)
    algorithm = StringVar()
    selection = algorithm.get()
    
    def run_hash():
        if selection == 'SHA 224 bit':
            encryption = 'hashlib.sha224(entered_text.encode())'
            hashed_string = hashlib.sha224(entered_text.encode())
        elif selection == 'SHA 256 bit':
            encryption = 'hashlib.sha256(entered_text.encode())'
            hashed_string = hashlib.sha256(entered_text.encode())
        elif selection == 'SHA 384 bit':
            encryption = 'hashlib.sha384(entered_text.encode())'
            hashed_string = hashlib.sha384(entered_text.encode())
        elif selection == 'SHA 512 bit':
            encryption = 'hashlib.sha512(entered_text.encode())'
            hashed_string = hashlib.sha512(entered_text.encode())
        elif selection == 'Blake2s':
            encryption = 'hashlib.blake2s(entered_text.encode())'
            hashed_string = hashlib.blake2s(entered_text.encode())
        elif selection == 'SHA3 256 bit':
            encryption = 'hashlib.sha3_256(entered_text.encode())'
            hashed_string = hashlib.sha3_256(entered_text.encode())
        elif selection == 'SHA3 384 bit':
            encryption = 'hashlib.sha3_384(entered_text.encode())'
            hashed_string = hashlib.sha3_384(entered_text.encode())
        elif selection == 'SHA3 512 bit':
            encryption = 'hashlib.sha3_512(entered_text.encode())'
            hashed_string = hashlib.sha3_512(entered_text.encode())
        elif selection == 'Blake2b':
            encryption = 'hashlib.blake2b(entered_text.encode())'
            hashed_string = hashlib.blake2b(entered_text.encode())
        elif selection == 'MD5':
            encryption = 'hashlib.md5(entered_text.encode())'
            hashed_string = hashlib.md5(entered_text.encode())
        elif selection == '':
            messagebox.showinfo(title='No Algorithm Error!', message='No hash algorithm was selected!')
        elif entered_text == '':
            messagebox.showinfo(title='No Data Error!', message='No data was entered to hash!')
            output.insert(END,'String Hashed: EMPTY\n' + 'Algorithm Type: ' + selection + '\nHash:' + hashed_string.hexdigest())
            
        else: output.insert(END,'String Hashed: ' + entered_text + '\n' + 'Algorithm Type: ' + selection + '\nHash:' + hashed_string.hexdigest())

    #exit program
    def close_window():
        window.destroy()
        exit()

    #about page
    def about():
        about_window = Tk()
        about_window.title('About Hash Algorithm Application')
        about_window.geometry("240x110+100+100")
        about_window.configure(background='black')
        info = Label(about_window, text='This app was created using\n* Python 3 *\n* hashlib & tkinter *\nDeveloped by: MB*Honey*Badger\nJuly 5th 2018',
              bg='black', fg='lawngreen', font='none 10 bold') .grid(row=0, column=1, sticky=N)
        #info.config(justify = CENTER)
        #python_logo = PhotoImage(file='guy.gif')
        #Label(about_window, image=python_logo, bg='black') .grid(row=3, column=0, sticky=W)

    #******************************************************************
    #button functions
    #def set_crypto():
    def set_sha_224():
        encryption = 'hashlib.sha224(entered_text.encode())'
    def set_sha_256():
        encryption = 'hashlib.sha256(entered_text.encode())'
    def set_sha_384():
        encryption = 'hashlib.sha384(entered_text.encode())'
    def set_sha_512():
        encryption = 'hashlib.sha512(entered_text.encode())'
    def set_blake2s():
        encryption = 'hashlib.blake2s(entered_text.encode())'
    def set_sha3_256():
        encryption = 'hashlib.sha3_256(entered_text.encode())'
    def set_sha3_384():
        encryption = 'hashlib.sha3_384(entered_text.encode())'
    def set_sha3_512():
        encryption = 'hashlib.sha3_512(entered_text.encode())'
    def set_blake2b():
        encryption = 'hashlib.blake2b(entered_text.encode())'
    def set_md5():
        encryption = 'hashlib.md5(entered_text.encode())'

    # toolbar functions ********************
    # column one, 'File' ******************
    def tb_new_project():
            print('still working on it')
            
    def tb_new():
            print('still working on it')

    def tb_save():
            print('still working on it')

    def tb_open():
            print('still working on it')
            
    def close_application():
            exit()
    # column two, 'Edit' ******************
    def tb_undo():
            print('still working on it')

    def tb_redo():
            print('still working on it')

    # password checker logic function *****
    def check_password():
        print('still working on it')

    # password checker window *************
    def tb_pass_check():
            password_checker_window = Tk()
            password_checker_window.title('Hash App - Password Checker')
            password_checker_window.geometry("500x310+100+100")
            password_checker_window.resizable(False, False)
            password_checker_window.configure(background='red')
            info = Label(password_checker_window, text='Password Checker', bg='black', fg='lawngreen', font='none 10 bold') .place(x=180, y=10)
            pass_entry = Entry(password_checker_window, width=55, bg='white')
            pass_entry.place(x=20, y=100)
            check_pass_button = Button(password_checker_window, text='Check Password', width=14, bg='black', fg='red', activebackground='red',
                                       command=check_password) .place(x=370, y=96)
            pass_output = Text(password_checker_window, width=60, height=8, wrap=WORD, background='white')
            pass_output.place(x=5, y=140)

    # toolbar *****************************
    toolbar = Menu(window)
    window.config(menu = toolbar)
    toolbar.configure(background='red')# not working

    # column one ******************************************************
    subMenu1 = Menu(toolbar)
    toolbar.add_cascade(label='File', menu=subMenu1)
    subMenu1.configure(background='whitesmoke')
    # options
    subMenu1.add_command(label='New Project...', command=tb_new_project)
    subMenu1.add_command(label='New', command=tb_new)
    subMenu1.add_command(label='Save', command=tb_save)
    subMenu1.add_command(label='Open', command=tb_open)
    subMenu1.add_separator()
    subMenu1.add_command(label='Exit', command=close_application)

    # column two ******************************************************
    subMenu2 = Menu(toolbar)
    toolbar.add_cascade(label='Edit', menu=subMenu2)
    subMenu2.configure(background='whitesmoke')
    # options
    subMenu2.add_cascade(label='Undo', command=tb_undo)
    subMenu2.add_cascade(label='Redo', command=tb_redo)
    subMenu2.add_separator()

    # column three ****************************************************
    subMenu3 = Menu(toolbar)
    toolbar.add_cascade(label='Tools', menu=subMenu3)
    subMenu3.configure(background='whitesmoke')
    # options
    subMenu3.add_cascade(label='Password Checker', command=tb_pass_check)
    subMenu3.add_cascade(label='Rainbow Table', command=tb_pass_check)
    subMenu3.add_separator()
    subMenu3.add_cascade(label='About Hash App', command=about)

    # main window objects *********************************************
    logo = PhotoImage(file='hb.gif')
    Label (window, image=logo, bg='black') .place(x=200, y=40)

    Label (window, text='Hash Generator Application', bg='black', fg='white', font='none 12 bold') .place(x=200, y=10)

    Label (window, text='Enter a string to hash', bg='black', fg='white', font='none 10 bold') .place(x=360, y=200)

    # buttons variables
    but1 = Radiobutton(window, text='SHA 224', width=10, bg='black', fg='red', activebackground='black', activeforeground='red',
                        command=set_sha_224, variable=algorithm, value='SHA 224 bit', cursor='spider') .place(x=5, y=55)# BUGS ALL OVER
    but2 = Radiobutton(window, text='SHA 256', width=10, bg='black', fg='red', activebackground='black', activeforeground='red',
                        variable=algorithm, value='SHA 256 bit', cursor='spider') .place(x=5, y=85)
    but3 = Radiobutton(window, text='SHA 384', width=10, bg='black', fg='red', activebackground='black', activeforeground='red',
                        variable=algorithm, value='SHA 384 bit', cursor='spider') .place(x=5, y=115)
    but4 = Radiobutton(window, text='SHA 512', width=10, bg='black', fg='red', activebackground='black', activeforeground='red',
                        variable=algorithm, value='SHA 512 bit', cursor='spider') .place(x=5, y=145)
    but5 = Radiobutton(window, text='Blake2s', width=10, bg='black', fg='red', activebackground='black', activeforeground='red',
                        variable=algorithm, value='Blake2s', cursor='spider') .place(x=5, y=175)
    but6 = Radiobutton(window, text='SHA3 256', width=10, bg='black', fg='red', activebackground='black', activeforeground='red',
                        variable=algorithm, value='SHA3 256 bit', cursor='spider') .place(x=90, y=55)
    but7 = Radiobutton(window, text='SHA3 384', width=10, bg='black', fg='red', activebackground='black', activeforeground='red',
                        variable=algorithm, value='SHA3 384 bit', cursor='spider') .place(x=90, y=85)
    but8 = Radiobutton(window, text='SHA3 512', width=10, bg='black', fg='red', activebackground='black', activeforeground='red',
                        variable=algorithm, value='SHA3 512 bit', cursor='spider') .place(x=90, y=115)
    but9 = Radiobutton(window, text='Blake2b', width=10, bg='black', fg='red', activebackground='black', activeforeground='red',
                        variable=algorithm, value='Blake2b', cursor='spider') .place(x=90, y=145)
    but10 = Radiobutton(window, text='MD5', width=10, bg='black', fg='red', activebackground='black', activeforeground='red',
                        variable=algorithm, value='MD5', cursor='spider') .place(x=90, y=175)

    submit_button = Button(window, text='Submit', width=6, bg='black', fg='red', activebackground='red', command=run_hash) .place(x=550, y=228)
    
    window.mainloop()

make_hash()




