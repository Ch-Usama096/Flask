import traceback
from flask import Flask
from flask import request , render_template , redirect , url_for

class ML:
    def __init__(self):
        self.avaliable_models = {
            "face_detection": "/additional_drive/ML/face_detection",
            "car_detection": "/additional_drive/ML/car_detection",
            "shoe_detection": "/additional_drive/ML/shoe_detection",
            "cloth_detection": "/additional_drive/ML/cloth_detection",
            "signal_detection": "/additional_drive/ML/signal_detection",
            "water_level_detection": "/additional_drive/ML/water_level_detection",
            "missile_detection": "/additional_drive/ML/missile_detection"
        }
        self.model_frequency = {
            "face_detection": 1,
            "car_detection": 1,
            "shoe_detection": 0,
            "cloth_detection":0,
            "signal_detection":0,
            "water_level_detection":0,
            "missile_detection":0
        }
        self.loaded_models_limit = 2
        self.loaded_models = {
            model: self.load_weights(model)
            for model in list(self.avaliable_models)[:self.loaded_models_limit]
        }
    
    def load_weights(self, model):
        return self.avaliable_models.get(model,None)

    def load_balancer(self, new_model):

        # Get the Models Key
        first_model  = list(self.loaded_models.keys())[0]
        second_model = list(self.loaded_models.keys())[1]

        # get the Frequnecy Values of Existing Model
        freq_first_model =  self.model_frequency[first_model]
        freq_second_model = self.model_frequency[second_model]


        freq_new_model = self.model_frequency[new_model] # Get the Frequency of new model
        freq_new_model += 1 # add the Frequency by using Processing
        self.model_frequency[new_model] = freq_new_model  # Add the new frequency of the model   
    
        if freq_first_model == freq_second_model:
           
            del self.loaded_models[first_model] # Delete the First Index Model
            self.loaded_models[new_model] = self.avaliable_models[new_model] # Add the New Model

        else:

            # Check which Model Frequency is Smaller
            get_small_model = lambda freq1 , freq2: first_model if freq1 < freq2 else second_model
            
            del self.loaded_models[get_small_model(freq_first_model , freq_second_model)] # Delete the Smaller Model
            self.loaded_models[new_model] = self.avaliable_models[new_model] # Add the New Model 

app = Flask(__name__)
ml = ML()

@app.route('/')
def printHome():
    return "Hello World"


@app.route('/get_loaded_models', methods=['GET', 'POST'])
def get_loaded_models():
    return ml.loaded_models

@app.route('/request_model')
def get_request_model():
    return render_template('requestModel.html')

@app.route('/process_request', methods=['GET', 'POST'])
def process_request():
    try:
        if request.method == 'POST':
            model = request.form['model']
            if model not in ml.loaded_models:
                ml.load_balancer(model)
                return ml.loaded_models
            else:
                return redirect(url_for('get_loaded_models')) # render the get_loaded_model when models same
    except:
        return str(traceback.format_exc())

#app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    app.run(debug=True)
