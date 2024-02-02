import random
from flask import Flask, render_template, request

MIN_PASSWORD_LENGTH = 12
UPPERCASE_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWERCASE_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SPECIAL_CHARACTERS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '.', '/', '<', '>', '?', '~', "'"]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    password = generate_password()
    if request.method == "GET":
        new_password = generate_password()
        return render_template('home.html', password=new_password)

    return render_template('home.html', password=password)


def generate_password():
    current_password_length = 0
    password = ""

    #Ensure that each password has at least one uppercase letter, one lowercase letter, one number and one special character.
    password += random.choice(UPPERCASE_LETTERS)
    password += random.choice(LOWERCASE_LETTERS)
    password += str(random.choice(NUMBERS))
    password += random.choice(SPECIAL_CHARACTERS)
    current_password_length = len(password)

    #Creates a pool of all of the possible characters that can be used for the password.
    pool = UPPERCASE_LETTERS + LOWERCASE_LETTERS + NUMBERS + SPECIAL_CHARACTERS

    #Fills out the rest of the password length with a random choice from the pool.
    while current_password_length < MIN_PASSWORD_LENGTH:
        password += str(random.choice(pool))
        current_password_length = len(password)

    print(password)
    
    shuffled_password = ''.join(random.sample(password, len(password)))

    return shuffled_password


generated_password = generate_password()
print(generated_password)

if __name__ == "__main__":
    app.run(debug=True)