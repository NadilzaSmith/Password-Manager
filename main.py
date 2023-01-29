#####################################
# UPGRADE USING JSON
#####################################
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for l in range(nr_letters)]
    password_symbols = [random.choice(symbols) for s in range(nr_symbols)]
    passoword_numbers = [random.choice(numbers) for n in range(nr_numbers)]

    password_list = password_letters + password_symbols + passoword_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website= website_entry.get()
    email=id_entry.get()
    password=password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password":password,

        }
    }

    empty_box = len(website) == 0 or len(password) == 0

    if empty_box:
        messagebox.showerror(title="Oops",message= " Please don't leave any fields empty !" )

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)


        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file, indent= 4)

        else:
            data.update(new_data)

            with open("data.json","w") as data_file:


                json.dump(data,data_file,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Erros",message= "Unregistered Website")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword :{password}")
        else:
            messagebox.showinfo(title="Erros", message="Unregistered Website")


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Password Manager")
screen.config(padx=50,pady=50)


canvas = Canvas(width=200,height=200)
image_pass = PhotoImage(file="logo.png")
canvas.create_image(100, 100 , image=image_pass)
canvas.grid(column=1,row=0)

# LABEL

website_label = Label(text= "Website:")
website_label.grid(column=0,row=1)

id_label = Label(text="Email/Username:")
id_label.grid(column=0,row=2 )

password_label = Label(text="Password:",width=15)
password_label.grid(column=0,row=3)


# ENTRY

website_entry = Entry(width=38)
website_entry.grid(column=1,row=1,columnspan=1)
website_entry.focus()

id_entry = Entry(width=57)
id_entry.grid(column=1,row=2,columnspan=3)
id_entry.insert(0, "nadilza.bastos@hotmail.com")


password_entry = Entry(width=38)
password_entry.grid(column=1,row=3,columnspan=1)

# BUTTON

botao1 = Button(text="Generate Password",command=password_generate,width=15)
botao1.grid(column=2,row=3)

botao2 = Button(text="Add",width=48,command=save)
botao2.grid(column=1,row=4,columnspan=3)

botao3= Button(text="Search",width=15,command=find_password)
botao3.grid(row=1,column=2)

screen.mainloop()