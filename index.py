from os import name
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

# Criando a janela
jan = Tk()

jan.title("Systems - Access Panel")
jan.geometry("600x300")
jan.configure(background='white')
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
# IMPORTANTE, AQUI MUDA COM RELAÇÃO AO WIN: (não pareceu nada de icone)
jan.iconbitmap('@/home/alessandro/Documentos/login/icons/login.xbm')

# =====Carregar imagem
logo = PhotoImage(file="icons/logo.png")

# ============= Wigets==================
LeftFrame = Frame(jan, width=200, height=300,
                  bg="WHITE", relief="raise")
LeftFrame.pack(side=LEFT)


RightFrame = Frame(jan, width=395, height=300,
                   bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)


LogoLabel = Label(LeftFrame, image=logo, bg="WHITE")
LogoLabel.place(x=2, y=25)  # 'x' é a posição lateral e o 'y' é a altura

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20),
                  bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=25)
UserEntry.place(x=155, y=110)
# -----
PasswordLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20),
                      bg="MIDNIGHTBLUE", fg="White")
# posição do login
PasswordLabel.place(x=5, y=150)
# caixa de entrada password
PasswordEntry = ttk.Entry(RightFrame, width=25, show='*')
PasswordEntry.place(x=155, y=160)


# Funções do Botão login.
def Login():
    User = UserEntry.get()
    Password = PasswordEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users 
    WHERE (User = ? AND Password = ?)
    """, (User, Password))
    print("selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()

    try:
        if User in VerifyLogin and Password in VerifyLogin:
            messagebox.showinfo(title="Login info",
                                message="Access confirm. Welcome!")
    except:
        messagebox.showerror(
            title="Login info", message="Access denied. Verify your login and password.")


# Botão login, front-end
LoginButton = ttk.Button(RightFrame, text="Login", width=20,  command=Login)
LoginButton.place(x=100, y=210)


# funções ao acessar a opção register
def Register():
    # removendo widgets de login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    # widgets de cadastro
    nomeLabel = Label(RightFrame, text="Name:", font=(
        "Century Gothic", 20), bg='MIDNIGHTBLUE', fg='white')
    nomeLabel.place(x=5, y=5)

    nomeEntry = ttk.Entry(RightFrame, width=30)
    nomeEntry.place(x=100, y=15)

    emailLabel = Label(RightFrame, text="Email:", font=(
        "Century Gothic", 20), bg='MIDNIGHTBLUE', fg='white')
    emailLabel.place(x=5, y=55)

    emailEntry = ttk.Entry(RightFrame, width=30)
    emailEntry.place(x=100, y=66)

    # registrando as informações no BD

    def RegisterToDataBase():
        name = nomeEntry.get()
        email = emailEntry.get()
        user = UserEntry.get()
        password = PasswordEntry.get()
        # Impedindo valores vazios em quais quer dos campos

        if (name == "" or email == "" or user == "" or password == ""):
            messagebox.showerror(title="Register error",
                                 message="Fill in all the fields! No empty fields.")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (name, email, user, password))
            DataBaser.conn.commit()  # salva alteração dos dadaos a cima no BD
            messagebox.showinfo(title="Register info",
                                message="Register Sucessful!")

    # Criando botão de salvar dados
    Register = ttk.Button(RightFrame, text='Save Data',
                          width=20, command=RegisterToDataBase)
    Register.place(x=100, y=210)

    def BackTologin():
        # removendo wigets de cadastro
        nomeLabel.place(x=5000)
        nomeEntry.place(x=5000)
        emailLabel.place(x=5000)
        emailEntry.place(x=5000)
        Register.place(x=5000)
        back.place(x=5000)
        # trazendo de volta os widgets de login
        LoginButton.place(x=100)
        RegisterButton.place(x=100)
        UserEntry.delete(0, END)
        PasswordEntry.delete(0, END)

    back = ttk.Button(RightFrame, text='Back', width=20, command=BackTologin)
    back.place(x=100, y=260)


RegisterButton = ttk.Button(
    RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=100, y=260)

jan.mainloop()
