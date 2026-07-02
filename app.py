import os
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load models safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    ridge_model = pickle.load(open(os.path.join(BASE_DIR, 'Models', 'ridge_model.pkl'), 'rb'))
    standard_scaler = pickle.load(open(os.path.join(BASE_DIR, 'Models', 'scaler.pkl'), 'rb'))
except Exception as e:
    print(f"Error loading models: {e}")
    ridge_model = None
    standard_scaler = None

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            # Extract inputs in the exact order required by the model
            Region = float(request.form.get('Region'))
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))

            # Scale data and predict
            new_data_scaled = standard_scaler.transform([[Region, Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes]])
            result = ridge_model.predict(new_data_scaled)[0]
            fwi_score = round(result, 2)

            # Risk Classification for UI
            if fwi_score < 5:
                risk = "Very Low Risk"
                alert_class = "alert-success"
                recommendation = "Safe conditions. Routine monitoring."
            elif fwi_score < 15:
                risk = "Low Risk"
                alert_class = "alert-warning"
                recommendation = "Avoid burning dry leaves."
            elif fwi_score <= 30:
                risk = "Moderate Risk"
                alert_class = "alert-orange" # Custom CSS class
                recommendation = "Stay Alert. Avoid campfires."
            else:
                risk = "High Risk"
                alert_class = "alert-danger"
                recommendation = "Emergency! Avoid forest entry and notify authorities."

            return render_template('home.html', result=fwi_score, risk=risk, alert_class=alert_class, recommendation=recommendation)
        
        except Exception as e:
            # This prints the real error in your terminal/command prompt
            print(f"ACTUAL BACKEND ERROR: {e}") 
            
            # This shows the real error on the web page instead of the generic message
            return render_template('index.html', error=f"System Error: {str(e)}")
    
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)