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

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == "POST":
        password = request.form['password']
        if verify_password(password):
            return render_template('verify.html', password=password, result="Valid Password!")
        else:
            return render_template('verify.html', password=password, result="Invalid Password!")

    return render_template('verify.html', password=None, result=None)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


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

def verify_password(password):
    if check_length(password) and check_contains_required_characters(password):
        return True
    return False


def check_length(password):
    return len(password) >= MIN_PASSWORD_LENGTH

def check_contains_required_characters(password):
    if any(substring in password for substring in UPPERCASE_LETTERS) and any(substring in password for substring in LOWERCASE_LETTERS) and any(str(substring) in password for substring in NUMBERS) and any(substring in password for substring in SPECIAL_CHARACTERS):
        return True
    return False



generated_password = generate_password()
print(generated_password)

if __name__ == "__main__":
    app.run(debug=True)