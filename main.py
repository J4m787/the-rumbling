from flask import Flask, render_template, request, flash, redirect, url_for, abort
import models
from flask_sqlalchemy import SQLAlchemy
from flask_login import logout_user, login_user, LoginManager, current_user, login_required
from forms import LoginForm, RegistrationForm



app=Flask(__name__)

app.config['SECRET_KEY'] = 'Ligmaballz!!!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return models.User.query.get(int(id))

@app.route("/")
def home():
    return render_template('home.html')
@app.route("/Adidas")
def Adidas():
    return render_template('Jordans.html')
@app.route("/Jordans")
def Jordans():
    return render_template('Jordans.html')
@app.route("/Nike")
def Nike():
    return render_template('Nike.html')
@app.route("/Others")
def Others():
    return render_template('Others.html')
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/search", methods=["POST"])
def search():
    # searchbar.
    # searches for anything that is similar to whatever the user inputted.
    results = models.shoe.query.filter(models.shoe.name.query.like('%' + request.form.get("filter") + '%'))
    return render_template("searchresults.html", title="Search Results", results=results)

@app.route("/searchbar", methods=["POST"])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('wrong password or username')
        else:
            login_user(user, remember=form.remember_me.data)
            flash('Logged in successfully.')
        next = request.args.get('next')
        return redirect(next or url_for('home'))
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = models.User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now a registered user.')
        login_user(user)
        return redirect(url_for('home'))
    return render_template("register.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/pizza/<int:id>')
def pizza(id):
        pizza= db.pizza.query.filter_by(id=id).first_or_404()
        return render_template('pizza.html',pizza=pizza)

if __name__ == "__main__":
    app.run(debug=True)


