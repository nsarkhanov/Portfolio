from flask import Blueprint, render_template
pages = Blueprint('pages', __name__)


@pages.route('/')
def home():
    return render_template('home.html')


@pages.route('/projects')
def projects():
    return render_template('projects.html')


@pages.route('/about')
def about():
    return render_template('about.html')


@pages.route('/blog')
def blog():
    return render_template('blog.html')


@pages.route('/contact')
def contact():
    return render_template('contact.html')
