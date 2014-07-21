import os, md5
from flask import Flask, session, redirect, url_for, request, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static', static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	login = db.Column(db.String(255), unique=True)
	password = db.Column(db.String(255))

	def __init__(self, login, password):
		self.login = login
		self.password = password

@app.route("/")
def index():
	if 'login' in session:
		return render_template('index.html', login=session['login'])
	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        result = User.query.filter(User.login == request.form['login'], User.password == md5.new(request.form['password']).hexdigest()).all()

        if len(result) == 1:
        	session['login'] = result[0].login
        	return redirect(url_for('index'))

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = User(request.form['login'], md5.new(request.form['password']).hexdigest())
        db.session.add(user)
        db.session.commit()
        session['login'] = user.login
        return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('index'))

app.secret_key = 'YouDontKnowMySecret'

@app.route('/redirectToApp')
def redirect_to_app():
	if 'login' in session:
		return redirect('followapp://login/%s' % session['login'])
	return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)