from flask import Flask, render_template, request
from FinalModel import predict_furnace_temps

app = Flask(__name__)

@app.route("/")
def home_page():
    # Default values for input fields
    default_inputs = {
        'width': '',
        'thickness': '',
        'gsm_a': '',
        'tph': ''
    }
    return render_template("Form.html", inputs=default_inputs)

@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Retrieve inputs from the form
        width = float(request.form['width'])
        thickness = float(request.form['thickness'])
        gsm_a = float(request.form['gsm_a'])
        tph = float(request.form['tph'])

        # Pass inputs for prediction
        result = predict_furnace_temps(width, thickness, gsm_a, tph)

        # Round the results to 2 decimal places
        result = {k: round(float(v), 2) for k, v in result.items()}

        # Pass inputs and results to output page
        inputs = {
            'width': width,
            'thickness': thickness,
            'gsm_a': gsm_a,
            'tph': tph
        }
        return render_template("output.html", result=result, inputs=inputs)

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)