from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
# write_key()
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key



key = load_key()
fer = Fernet(key)
  


# b'hello' --> bytes string different from normal string

def add():


    name = input("Account name")
    pwd = input("PASSWORD")
    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


def view():


    with open("password.txt", "r") as f:
        for line in f.readlines():

           data = line.rstrip()
           user, passw = data.split("|")
           print("username", user , "password", fer.decrypt(passw.encode()).decode())





while True:

    mode = input("Would you like to add a new password or view existing ones (add/view), q to quit").lower()


    if mode == "q":
        break


    if mode == "view":
        view()


    elif mode == "add":
        add()
    else:
        print("Invalid")
        continue





# Here’s a detailed explanation of how this  code encrypts and decrypts passwords:

# ---

# ### 1. **Encryption (Storing the Password)**

# - When you call `add()`, the user enters an account name and a password.
# - The password is encrypted using this line:
#   ```python
#   fer.encrypt(pwd.encode()).decode()
#   ```
#   - `pwd.encode()` converts the password (a string) into bytes, which is required for encryption.
#   - `fer.encrypt(...)` uses the Fernet object (created with your secret key) to encrypt the bytes. This produces an encrypted byte string (ciphertext).
#   - `.decode()` converts the encrypted bytes back into a string so it can be saved in a text file.
# - The code then writes a line to password.txt:
#   ```
#   account_name|encrypted_password
#   ```
#   For example, if the account is "gmail" and the password is "mypassword", the file might contain:
#   ```
#   gmail|gAAAAABk... (a long string of random-looking characters)
#   ```
#   The encrypted password is unreadable without the key.

# ---

# ### 2. **Decryption (Viewing the Password)**

# - When you call `view()`, the code reads each line from password.txt.
# - It splits each line into `user` (the account name) and `passw` (the encrypted password string).
# - To decrypt, it uses:
#   ```python
#   fer.decrypt(passw.encode()).decode()
#   ```
#   - `passw.encode()` turns the encrypted string back into bytes.
#   - `fer.decrypt(...)` uses the Fernet object (with your secret key) to decrypt the bytes, turning them back into the original password bytes.
#   - `.decode()` converts the bytes back into a readable string (the original password).
# - The code then prints the account name and the decrypted password.

# ---

# ### 3. **Why is this secure?**

# - The password is never stored in plain text. Only the encrypted version is saved.
# - Without the correct key (from key.key), the encrypted password cannot be decrypted.
# - Even if someone opens password.txt, they cannot see your real passwords.

# ---

# **Summary:**  
# - **Encryption:** Converts your password into unreadable text using your secret key before saving.
# - **Decryption:** Converts the unreadable text back into your real password using the same key when you want to view it.

# Let me know if you want a step-by-step example with sample data!