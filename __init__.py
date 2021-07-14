from flask import Flask, render_template, request, url_for, redirect
from get_form import create_form
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['fullname']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        print(name, email, subject, message)
        create_form(name, email, subject, message)
        return render_template('contact.html')

    else:
        return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
