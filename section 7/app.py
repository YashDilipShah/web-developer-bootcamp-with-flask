from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/expressions/')
def hello():

    #interpolation
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"


    #addition and substraction
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15 

    # string concantenation
    first_name = "Captain"
    last_name = "Marvel"



    """
    return render_template(
        "expressions.html", 
        color=color,
        animal_one=animal_one,
        animal_two=animal_two,
        orange_amount=orange_amount,
        apple_amount=apple_amount,
        donate_amount=donate_amount,
        first_name=first_name,
        last_name=last_name,
        render="Jinja"
    )
    """
    
    #We can do this, or we can use dictionary

    kwargs = {
        "color" : color, 
        "animal_one" : animal_one, 
        "animal_two" : animal_two,
        "orange_amount" : orange_amount, 
        "apple_amount" : apple_amount,
        "donate_amount" : donate_amount,
        "first_name" : first_name,
        "last_name" : last_name
    }

    return render_template(
        "expressions.html", **kwargs
    )

    

app.run(debug=True, port=5000)