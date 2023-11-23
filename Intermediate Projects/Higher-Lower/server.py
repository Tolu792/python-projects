from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route('/')
def home_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp" alt="gif-image">'


@app.route('/<int:number>')
def guess(number):
    if number > random_number:
        return '<h1 style="color: purple">Too High, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="gif-image">'
    elif number < random_number:
        return '<h1 style="color: red">Too Low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="gif-image">'
    else:
        return '<h1 style="color: green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="gif-image">'


if __name__ == "__main__":
    app.run(debug=True)
