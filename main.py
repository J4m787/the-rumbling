from flask import Flask, render_template, request, flash, redirect, url_for, abort
import models
from flask_sqlalchemy import SQLAlchemy
from flask_login import logout_user, login_user, LoginManager, current_user, login_required
from forms import LoginForm, RegistrationForm


app=Flask(__name__)

app.config['SECRET_KEY'] = 'IRD'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app, session_options={'autoflush': False})
login_manager = LoginManager()
login_manager.init_app(app) 

@login_manager.user_loader
def load_user(id):
    return models.User.query.get(int(id))


# route for home
@app.route("/")
def home():
    return render_template('home.html')


# route renders the Jordans page
@app.route("/brand/<int:id>")
def brand(id):
    results = models.Brand.query.filter_by(id=id).first()
    return render_template('brand.html', results=results)


# route renders the Jordans 2 page
@app.route("/silhouette/<int:id>")
def silhouette(id):
    user = models.User.query.filter_by(id=current_user.id).first_or_404()
    results = models.Silhouette.query.filter_by(id=id).first()
    return render_template('table.html', results=results, user=user)


@app.route("/my_favourites", methods=["GET", "POST"])
@login_required  # requires user to be logged in to add favourite
def favourites():
    results = models.User.query.filter_by(id=current_user.id).first_or_404()
    user = models.User.query.filter_by(id=current_user.id).first_or_404()
    
    return render_template('table.html', results=results, user=user, title="My Favourite Shoes")


# Route to add shoe to favourites table
@app.route("/favourite/<int:id>", methods=["GET", "POST"])
@login_required  # requires user to be logged in to add favourite
def favourite(id):
    # Adds favourite shoe by assigining current user id to user id table
    # and adds the shoe id to shoes id table.
    user = models.User.query.filter_by(id=current_user.id).first_or_404()
    shoe = models.Shoe.query.filter_by(id=id).first()
    user.shoes.append(shoe)
    db.session.merge(user)
    db.session.commit()
    return redirect(url_for("silhouette", id=shoe.silhouette.id))


# route to remove a game from your favourites
@app.route("/delete/<int:id>", methods=["GET", "POST"])
@login_required # requires user to be logged in to remove a favourited game
def delete(id):
    user = models.User.query.filter_by(
        id=current_user.id
    ).first_or_404()
    shoe = models.Shoe.query.filter_by(id=id).first_or_404()
    user.shoes.remove(shoe)
    db.session.merge(user)
    db.session.commit()
    return redirect(url_for("favourites"))


# route allows user to login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # sends user back to home if logged in
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        # if the password or the email doesn't exist tell the user
        if user is None or not user.check_password(form.password.data):
            flash('wrong password or email')
        else:
            # login user if information is correct
            login_user(user, remember=form.remember_me.data)
            flash('Logged in successfully.')
            next = request.args.get('next')
            return redirect(next or url_for('home'))
    return render_template('login.html', form=form)


# route allows user to register
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        # if it already exists it tells them
        if user is not None:
            flash('User already exists')
        else:
            # puts email, and password into the database
            user = models.User(email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('You are now a registered user.')
            return redirect(url_for('login'))
    return render_template("register.html", form=form)


# logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
