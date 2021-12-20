from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    first_name = "John"
    stuff = "This is Bold Text"
    favourite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html", first_name=first_name,
                           stuff=stuff, favourite_pizza=favourite_pizza)


@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)


#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Invalid Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
    