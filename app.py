from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bdfghnskjroejrg54htjyk5420ktj504eh5e0h'
app.config['SQLALCHEMY_DB_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

 # I put it here so that it could see db before importing models
from models import User, Post

post=[
    {
        'title': 'Things you must do in life',
        'author': 'Abass',
        'date_created': '22nd January 2020',
        'content': 'This life is so soft when you have not cut connection between you and God'
    },
    {
        'title': 'Abass is got to win',
        'author': 'Adekunle',
        'date_created': '23rd January 2019',
        'content': 'This life is so soft when you have not cut connection between youu and God'
    },
    {
        'title': 'This is getting interesting',
        'author': 'Abass',
        'date_created': '22nd January 2020',
        'content': 'This life is so soft when you have not cut connection between youu and God'
    },
    {
        'title': 'We need to be consistent in our life',
        'author': 'Makinde',
        'date_created': '22nd January 2020',
        'content': 'This life is so soft when you have not cut connection between youu and God'
    },
    {
        'title': 'How to get rich within a week',
        'author': 'Abs',
        'date_created': '2nd March 2000',
        'content': 'This life is so soft when you have not cut connection between youu and God'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=post)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(('Account sussesfully created for {0}!').format(form.username.data), 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login',  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'abs@blog.com' and form.password.data == 'password':
            flash('Logged in succesfully', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unseccessful check your login credentials', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)