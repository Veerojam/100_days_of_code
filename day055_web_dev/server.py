from flask import Flask
import random


rand_int = random.randint(0, 9)

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <div style="text-align: center;">
    <h1>Guess a number between 0 and 9<h1/>
    <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">
    </div>
    '''

@app.route('/<int:guess>')
def guessing(guess):
    if guess == rand_int:
        return '''
        <div style="text-align: center; color: green;">
        <h2> You found me!</h2>
        <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">
        </div>
        '''
    elif guess < rand_int:
        return '''
        <div style="text-align: center; color: crimson;">
        <h2> Too low, keep digging!</h2>
        <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWF3aG91dTFtNDl1ZGd5enZuZnk1d3h2YWd6ZDN4Y2ZmMWpwZG1nayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jD4DwBtqPXRXa/giphy.gif" height=500 width=500>
        </div>
        '''
    else:
        return '''
        <div style="text-align: center; color: crimson;">
        <h2> Too high!<h2/>
        <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">
        </div>
        '''



# if __name__ == "__main__":
#     app.run(debug=True)
