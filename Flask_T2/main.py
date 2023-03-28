# Creating the Modules 

from flask import Flask , redirect , url_for , render_template


# Creating the Object of Flask (WSGI)
app = Flask(__name__)

# Creating the First Decorator
@app.route('/')
def printHome():
    return render_template('index.html')

# Creating the Second Decorator
@app.route('/service')
def printService():
    return render_template('service.html')

# Creating the Third Decorator
@app.route('/help')
def printHelp():
    return render_template('help.html')


# Main Part of the Flask App
if __name__ == "__main__":
    app.run()
