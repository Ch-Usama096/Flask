# Import the Modules
from flask import Flask , render_template , request , redirect , url_for

# Creating the Object of the Flask (WSGI)
app = Flask(__name__)

# Creating the First Decorator
@app.route('/')
def printHome():
    return render_template('home.html')

# Creating the Second Decorator
@app.route('/pass/<int:score>')
def printPass(score):
    return render_template('pass.html' , result = score)

# Creating the Third Decorator
@app.route('/fail/<int:score>')
def printFail(score):
    return render_template('fail.html' , result = score)

@app.route('/submit' , methods = ['POST' , 'GET'])
def printSubmit():
    result = 0
    if request.method == 'POST':
        dataScience     = float(request.form['dataScience'])
        machineLearning = float(request.form['machineLearning'])
        deepLearning    = float(request.form['machineLearning'])
        computerVision  = float(request.form['computerVision'])
        # Find the Average Score of All Subjects
        result = int((dataScience + machineLearning + deepLearning + computerVision) / 4)
        checker = ""
        # Check the Student Fail or Pass
        if result >= 60:
            checker = "printPass"
        else:
            checker = 'printFail'

        return redirect(url_for(checker , score = result))


# Main Part of the Flask App
if __name__ == "__main__":
    app.run(debug=True)