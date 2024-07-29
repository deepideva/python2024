from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>BMI Calculator</title>
    </head>
    <body>
        <h1>BMI Calculator</h1>
        <form action="/calculate" method="post">
            <label for="height">Height (in meters):</label>
            <input type="text" id="height" name="height"><br><br>
            <label for="weight">Weight (in kilograms):</label>
            <input type="text" id="weight" name="weight"><br><br>
            <input type="submit" value="Calculate BMI">
        </form>
    </body>
    </html>
    ''')

@app.route('/calculate', methods=['POST'])
def calculate():
    height = float(request.form['height'])
    weight = int(request.form['weight'])
    bmi = weight / (height * height)
    if bmi < 18.5:
        result = f"Your BMI is {bmi}, you are underweight."
    elif bmi < 25:
        result = f"Your BMI is {bmi}, you have a normal weight."
    elif bmi < 30:
        result = f"Your BMI is {bmi}, you are slightly overweight."
    elif bmi < 35:
        result = f"Your BMI is {bmi}, you are obese."
    else:
        result = f"Your BMI is {bmi}, you are clinically obese."

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>BMI Calculator</title>
    </head>
    <body>
        <h1>BMI Calculator</h1>
        <p>{{ result }}</p>
        <a href="/">Calculate again</a>
    </body>
    </html>
    ''', result=result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
