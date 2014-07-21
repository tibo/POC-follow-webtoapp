import os, md5
from flask import Flask, session, redirect, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
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
		return 'hello %s <br /> <a href="/logout">Logout</a>' % session['login']
	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        result = User.query.filter(User.login == request.form['login'], User.password == md5.new(request.form['password']).hexdigest()).all()

        if len(result) == 1:
        	session['login'] = result[0].login
        	return redirect(url_for('index'))

        return redirect(url_for('login'))

    return '''
        <form action="" method="post">
            <p>Login: <input type="text" name="login" /></p>
            <p>Password: <input type="password" name="password" /></p>
            <p><input type="submit" value="Login" /></p>
        </form>
        No Account? <a href="/signup">Sign Up</a>
        '''

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = User(request.form['login'], md5.new(request.form['password']).hexdigest())
        db.session.add(user)
        db.session.commit()
        session['login'] = user.login
        return redirect(url_for('index'))
    return '''
    	New account
        <form action="" method="post">
            <p>Login: <input type="text" name="login" /></p>
            <p>Password: <input type="password" name="password" /></p>
            <p><input type="submit" value="Signup" /></p>
        </form>
        '''

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