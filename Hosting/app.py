from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Home Page</title>
    </head>
    <body>
        <h1>Welcome to the Multi-Page Flask App</h1>
        <ul>
            <li><a href="/pizza">Pizza Order App</a></li>
            <li><a href="/bmi">BMI Calculator App</a></li>
            <li><a href="/wonderla">Wonderla Tickets App</a></li>
        </ul>
    </body>
    </html>
    ''')

@app.route('/pizza', methods=['GET', 'POST'])
def pizza_order():
    if request.method == 'POST':
        size = request.form['size']
        add_pepperoni = request.form['add_pepperoni']
        extra_cheese = request.form['extra_cheese']
        bill = 0
        if size == 'S':
            bill = 15
            if add_pepperoni == 'Y':
                bill += 2
            if extra_cheese == 'Y':
                bill += 1
        elif size == 'M':
            bill = 20
            if add_pepperoni == 'Y':
                bill += 3
            if extra_cheese == 'Y':
                bill += 1
        elif size == 'L':
            bill = 25
            if add_pepperoni == 'Y':
                bill += 3
            if extra_cheese == 'Y':
                bill += 1
        return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Pizza Order Result</title>
        </head>
        <body>
            <h1>Pizza Order App</h1>
            <p>Your final bill is: Rs {{ bill }}.</p>
            <a href="/pizza">Order another pizza</a><br>
            <a href="/">Back to Home</a>
        </body>
        </html>
        ''', bill=bill)
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Pizza Order App</title>
    </head>
    <body>
        <h1>Pizza Order App</h1>
        <form method="post">
            <label>What size pizza do you want? S, M, or L:</label>
            <input type="text" name="size"><br><br>
            <label>Do you want pepperoni? Y or N:</label>
            <input type="text" name="add_pepperoni"><br><br>
            <label>Do you want extra cheese? Y or N:</label>
            <input type="text" name="extra_cheese"><br><br>
            <input type="submit" value="Calculate Bill">
        </form>
        <a href="/">Back to Home</a>
    </body>
    </html>
    ''')

@app.route('/bmi', methods=['GET', 'POST'])
def bmi_calculator():
    if request.method == 'POST':
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
            <title>BMI Result</title>
        </head>
        <body>
            <h1>BMI Calculator App</h1>
            <p>{{ result }}</p>
            <a href="/bmi">Calculate again</a><br>
            <a href="/">Back to Home</a>
        </body>
        </html>
        ''', result=result)
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>BMI Calculator App</title>
    </head>
    <body>
        <h1>BMI Calculator App</h1>
        <form method="post">
            <label>Enter your height in meters:</label>
            <input type="text" name="height"><br><br>
            <label>Enter your weight in kilograms:</label>
            <input type="text" name="weight"><br><br>
            <input type="submit" value="Calculate BMI">
        </form>
        <a href="/">Back to Home</a>
    </body>
    </html>
    ''')

@app.route('/wonderla', methods=['GET', 'POST'])
def wonderla_tickets():
    if request.method == 'POST':
        height = int(request.form['height'])
        bill = 0
        if height >= 120:
            age = int(request.form['age'])
            if age < 12:
                bill = 5
            elif age <= 18:
                bill = 7
            else:
                bill = 12
            if request.form['want_photo'] == 'Y':
                bill += 3
            result = f"Your Final Bill is {bill}."
        else:
            result = "Get Out of Amusement park"
        return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Wonderla Tickets Result</title>
        </head>
        <body>
            <h1>Wonderla Tickets App</h1>
            <p>{{ result }}</p>
            <a href="/wonderla">Calculate again</a><br>
            <a href="/">Back to Home</a>
        </body>
        </html>
        ''', result=result)
    return render_template_string('''
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Wonderla Tickets App</title>
    </head>
    <body>
        <h1>Wonderla Tickets App</h1>
        <form method="post">
            <label>What is your height in cms?</label>
            <input type="text" name="height"><br><br>
            <label>What's your age?</label>
            <input type="text" name="age"><br><br>
            <label>Do you want a photo taken? Y or N:</label>
            <input type="text" name="want_photo"><br><br>
            <input type="submit" value="Calculate Bill">
        </form>
        <a href="/">Back to Home</a>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
