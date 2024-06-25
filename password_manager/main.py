from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
        
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
    


master_pwd = input("input your master password : ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def add():
    name = input("Account Name : ")
    pwd = input("Password : ")
    
    with open('password.txt','a') as f:
        f.write(name + " / " + str(fer.encrypt(pwd.decode())) + "\n") 

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pswd = data.split("/")
            print(f"User: {user} / pswd" , 
                  fer.encrypt(pwd.encode()).decode())
            

while True:
    mode = input("would you like to add a new password or view existing ones (view, add,q)").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue