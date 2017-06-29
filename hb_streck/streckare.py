import tkinter
from tkinter.constants import *
from abc import ABCMeta, abstractmethod

#with open('users.txt', 'r+') as user_db_raw :
#    all_users = []
#    for line in user_db_raw.readlines():
#        current_user = []
#        for element in line.split('.') :
#            current_user.append(element)
#        all_users.append(current_user)
#    print(all_users)
    
#def createStreckLista() :

def encrypt(pswrd) :
    encrypt_key = 0
    encrypted_string = []
    for letter in pswrd :
        encrypt_key += ord(letter)
    for letter in pswrd :
        encrypted_string.append(ord(letter) * encrypt_key)
    return encrypted_string

def decrypt(pswrd_enc) :
    decrypt_key_string = input("enter password: ")
    decrypted_string = ''
    decrypt_key = 0
    for letter in decrypt_key_string :
        decrypt_key += ord(letter)
    for letter in pswrd_enc :
        decrypted_string = decrypted_string + str(chr(int(letter / decrypt_key)))
    return decrypted_string

def enter_password(usr) :
    # find user in db n shit
    print('Enter password:')
    usr_pswrd = input()
    print("Confirm password:")
    usr_pswrd_confirm = input()
    if usr_pswrd != usr_pswrd_confirm :
        print("Password doesn't match, please try again.")
        return None
    else :
        return pswrd

def register_usr():
    print('Enter username: ')
    usr_wish = input()
    while usr_wish in user_db :
        print('Username already exists, please choose another')
        usr_wish = input()
    print('Valid username. Welcome ', usr_wish, "!")
    password = None
    while password == None :
        password = enter_password(usr_wish)


#class user(object) :
    """user that has access to Strecklista

attributes: username (str), password (str)"""
    
    ##def __init__ :
        
    
def update_streck_lista() :
    streck_lista_internal = []
    user_list_internal = []
    with open("db_streck.txt", 'r') as streck_lista_input :
        for line in streck_lista_input.readlines() :
            current_lista = []
            for tab in line.split('.') :
                #print(tab, type(tab))
                if len(current_lista) != 0 :
                    current_lista.append(int(tab))
                else :
                    current_lista.append(tab)
            streck_lista_internal.append(current_lista)
            user_list_internal.append(current_lista[0])
        l = 0
        for line in streck_lista_internal :
            total = 0
            for tab in line :
                if isinstance(tab,int) :
                    total += tab
            streck_lista_internal[l].append(total)
            l += 1
    return streck_lista_internal, user_list_internal

def main_menu() :
    main = tkinter.Tk()
    main_frame = tkinter.Frame(main, relief=RIDGE, borderwidth=5)
    main_frame.pack(fill=BOTH, expand=1)
    main_label = tkinter.Label(main_frame, text="Hornboskapens Ölstreckslista")
    main_label.pack(fill=X, expand=1)
    strecklista_button = tkinter.Button(main_frame, text="Visa strecklistan")
    strecklista_button.bind(sequence='<Button-1>', func=display_streck_lista())
    strecklista_button.pack(side=TOP, anchor=N)
    credits_button = tkinter.Button(main_frame, text="Credits")
    credits_button.pack(side=TOP, anchor=N)
    avsluta_button = tkinter.Button(main_frame, text="Avsluta",command=main.destroy)
    avsluta_button.pack(side=TOP, anchor=N)
    main.mainloop()

def display_streck_lista() :
    tk = tkinter.Tk()
    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=20)
    frame.pack(fill=BOTH,expand=1)
    label = tkinter.Label(frame, text="HB:s Ölstreckslista")
    label.pack(fill=X, expand=1)
    button = tkinter.Button(frame,text="Exit",command=tk.destroy)
    button.pack(side=RIGHT,anchor=E)
    

streck_lista, user_list = update_streck_lista()
print(streck_lista)

#password = input('enter password: ')
#password_encrypted = encrypt(password)
#print(password_encrypted)
#print(decrypt(password_encrypted))

#display_streck_lista()
main_menu()
