from flask import Flask , render_template , request
import hashlib

app = Flask(__name__)


# Create the First Decorator
@app.route('/')
def printHome():
    return "Hello Home Page"


# Create the Second Decorator (UserName)
@app.route('/userName/<string:username>')
def printUserName(username):
    return render_template('UserNameDisplay.html' , name = username)

# Create the Third Decorator (Square of Number)
@app.route('/numberSQ/<int:number>')
def printNumber(number):
    sq = number ** 2  # Calculate the Square of Number
    return render_template('SquareNumber.html' , res = sq , num = number)


# Create the Forth Decorator (Upload Image)
@app.route('/uploadImagePath')
def printImage():
    return  render_template('uploadImagePath.html')   # Get the Image from the User

# Create the Fifth Decorator (Convert Hash)
@app.route('/convertHash' , methods = ['GET' , 'POST'])
def printHash():
    if request.method == 'POST':
        image =   request.form['Path']
        # Convert the Image into md5Hash
        with open(image, "rb") as f:
            im_bytes = f.read()
        im_hash = str(hashlib.md5(im_bytes).hexdigest())
        return "<b>Here is the md5Hash of the Image :  </b>"+ im_hash


# Create the 

if __name__ == "__main__":
    app.run()