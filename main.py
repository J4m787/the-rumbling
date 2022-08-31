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

'''@app.context_processor
def context_processor():
    results = models.Silhouette.query.filter_by().order_by(models.Silhouette.id).all()
    return results'''

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/Jordans")
def Jordans():
    results = models.Silhouette.query.filter_by(brand_id=1).order_by(models.Silhouette.id).all()
    return render_template('Jordans.html', results=results)

    
@app.route("/Adidas")
def Adidas():
    results = models.Silhouette.query.filter_by(brand_id=2).order_by(models.Silhouette.name).all()
    return render_template('Adidas.html', results=results)

@app.route("/Nike")
def Nike():
    results = models.Silhouette.query.filter_by(brand_id=3).order_by(models.Silhouette.name).all()
    return render_template('Nike.html',  results=results)

@app.route("/Others")
def Others():
 results = models.Silhouette.query.filter_by(brand_id=4).order_by(models.Silhouette.name).all()
 return render_template('Others.html',  results=results)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/Jordan1")
def Jordan1():
    results = models.Shoe.query.filter_by(silhouette_id=1).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)

@app.route("/Jordan3")
def Jordan3():
    results = models.Shoe.query.filter_by(silhouette_id=2).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)


@app.route("/Jordan4")
def Jordan4():
    results = models.Shoe.query.filter_by(silhouette_id=4).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)

@app.route("/Jordan11")
def Jordan11():
    results = models.Shoe.query.filter_by(silhouette_id=5).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)

@app.route("/Yeezy350")
def Yeezy350():
    results = models.Shoe.query.filter_by(silhouette_id=6).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)

@app.route("/Yeezy500")
def Yeezy500():
    results = models.Shoe.query.filter_by(silhouette_id=7).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)

@app.route("/Yeezy700")
def Yeezy700():
    results = models.Shoe.query.filter_by(silhouette_id=8).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)

@app.route("/YeezySlides")
def YeezySlides():
    results = models.Shoe.query.filter_by(silhouette_id=9).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)

@app.route("/Af1")
def Af1():
    results = models.Shoe.query.filter_by(silhouette_id=11).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)

@app.route("/AirMax97")
def AirMax97():
    results = models.Shoe.query.filter_by(silhouette_id=12).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)

@app.route("/Blazer")
def Blazer():
    results = models.Shoe.query.filter_by(silhouette_id=13).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)

@app.route("/Nikesb")
def Nikesb():
    results = models.Shoe.query.filter_by(silhouette_id=10).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)

@app.route("/NB550")
def NB550():
    results = models.Shoe.query.filter_by(silhouette_id=14).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)

@app.route("/NB990")
def NB990():
    results = models.Shoe.query.filter_by(silhouette_id=15).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)

@app.route("/NB993")
def NB993():
    results = models.Shoe.query.filter_by(silhouette_id=16).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)

@app.route("/Converse")
def Converse():
    results = models.Shoe.query.filter_by(silhouette_id=17).order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)


@app.route("/table")
def table():
    results = models.Shoe.query.order_by(models.Shoe.name).all()
    return render_template('table.html', results=results)

@app.route("/search", methods=["POST"])
def search():
    # searchbar.
    # searches for anything that is similar to whatever the user inputted.
    results = models.Shoe.query.filter(models.Shoe.name.query.like('%' + request.form.get("filter") + '%'))
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


