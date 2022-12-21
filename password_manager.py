from cryptography.fernet import Fernet



'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)

write_key()
'''
def load_key():
    with open('key.key','rb') as keyfile:
        return keyfile.read()

main_password = input("Enter your password ").encode()
token = load_key() + main_password
Fer = Fernet(token)
def add():
    
    u_name = input("Enter your user name: ")
    u_psw = input("Enter your user password: ")
    with open('passwords.txt','a') as f:
        f.write(u_name+'|'+ Fer.decrypt(u_psw.encode()).decode()+'\n')


def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            user,passw = line.strip().split('|')
            print("Username : ",user,"\n","Password : ",Fer.decrypt(passw.encode()).decode())


while True:
    while True:
        mode = input("Would you like to manage password? Then type add/view or q to quit ").lower()
        if mode in ['q','add','view']:
            break
    if mode == 'q':
        break
    if mode == 'add':
      add()
      break
    else:
      view()
      break



