import os
import tkinter as tk
def register_user():
    email_info = email.get()
    password_info = password.get()
    
    #file writes info
    file =open(email_info, "w")
    file.write(email_info+'\n')
    file.write(password_info+'\n')
    file.close()
    
    created_email_entry.delete(0, tk.END)
    created_password_entry.delete(0, tk.END)
def login_user():
    email1 = email_verify.get()
    password1 = password_verify.get()
    entered_email.delete(0, tk.END)
    entered_password.delete(0, tk.END)
    
    list_of_files = os.listdir()
    if email1 in list_of_files:
     file1 =open(email1, "r")
     verify = file1.read().splitlines()
     if password1 in verify:
        print('login success')
     else:
        print('password has not been recognised')
    else:
        print("User not found")

    
#Functions for buttons
def fnc_menu_to_login():
    print('menu to login')
    mainmenu.pack_forget()
    login.pack()
def fnc_menu_to_create_new():
    print('main menu to create new')
    mainmenu.pack_forget()
    create_new.pack()
def fnc_login_to_menu():
    print('login to menu')
    login.pack_forget()
    mainmenu.pack()
def fnc_create_new_to_menu():
    print('create new to menu')
    create_new.pack_forget()
    mainmenu.pack()


root = tk.Tk() 
root.geometry('400x400')
global create_New_l1

# Frames:
mainmenu = tk.Frame(root, bg = "red")
login = tk.Frame(root, bg = "blue")
create_new = tk.Frame(root, bg = "green")


# Labels : 
mainmenu_l1 = tk.Label(mainmenu, text = "Main Menu")
login_l1 = tk.Label(login, text = "Login")
create_New_l1 = tk.Label(create_new, text = "Become a new user!")


# Buttons :
main_menu_to_login = tk.Button(mainmenu, text = 'Login', command= fnc_menu_to_login)
main_menu_to_create_new = tk.Button(mainmenu, text = 'Create New Account', command= fnc_menu_to_create_new)
login_to_menu = tk.Button(login, text = 'Main Menu', command= fnc_login_to_menu)
create_new_to_menu = tk.Button(create_new, text = 'Main Menu', command= fnc_create_new_to_menu)
register = tk.Button(create_new, text="Register", command=register_user)
loginbut = tk.Button(login, text="Login", command=login_user)
#Frame 1
mainmenu_l1.pack()

main_menu_to_login.pack()
main_menu_to_create_new.pack()

#Frame 2
global email_verify
global password_verify
login_l1.pack()
email_verify = tk.StringVar()
password_verify = tk.StringVar()
entered_email = tk.Entry(login, textvariable = email_verify)
entered_email.insert(0, "Email")
entered_email.pack()
entered_password = tk.Entry(login, textvariable = password_verify)
entered_password.insert(0, "Password")
entered_password.pack()
login_to_menu.pack()
loginbut.pack()

#Frame 3
create_New_l1.pack()
global email
global password
email = tk.StringVar()
password = tk.StringVar()
create_new_to_menu.pack()
created_email_entry = tk.Entry(create_new, textvariable = email)
created_email_entry.insert(0, "Enter your Email")
created_email_entry.pack()

created_password_entry = tk.Entry(create_new, textvariable = password)
created_password_entry.insert(1,"Enter your Password")
created_password_entry.pack()
register.pack()



mainmenu.pack()
root.mainloop()

