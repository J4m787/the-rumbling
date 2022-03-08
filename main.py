from flask import Flask, render_template

app=Flask(__name__)

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




if __name__ == "__main__":
    app.run(debug=True)
@app.route('/pizza/<int:id>')
def pizza(id):
        pizza= db.pizza.query.filter_by(id=id).first_or_404()
        return render_template('pizza.html',pizza=pizza)

