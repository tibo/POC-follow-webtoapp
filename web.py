import os, md5
from flask import Flask, session, redirect, url_for, request, render_template, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static', static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	login = db.Column(db.String(255), unique=True)
	password = db.Column(db.String(255))
	follow_key = db.Column(db.String(255))
	follow_source_ip = db.Column(db.String(255))

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
        results = User.query.filter(User.login == request.form['login'], User.password == md5.new(request.form['password']).hexdigest()).all()

        if len(results) == 1:
        	session['login'] = results[0].login
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

		if not request.headers.getlist("X-Forwarded-For"):
			ip = request.remote_addr
		else:
			ip = request.headers.getlist("X-Forwarded-For")[0]

		user = User.query.filter(User.login == session['login']).first()
		user.follow_key = os.urandom(10).encode('hex')
		user.follow_source_ip = ip

		db.session.commit()

		return redirect('followapp://%s' % user.follow_key)
	return redirect(url_for('login'))

@app.route('/getSession.json')
def get_session():

	if not request.headers.getlist("X-Forwarded-For"):
		ip = request.remote_addr
	else:
		ip = request.headers.getlist("X-Forwarded-For")[0]

	results = User.query.filter(User.follow_key == request.args.get('follow_key'), User.follow_source_ip == ip).all()

	if len(results) == 1:
		user = results[0]
		user.follow_key = None
		user.follow_source_ip = None

		db.session.commit()

		return jsonify({'login': user.login}), 200

	return jsonify({'error': 'not authorized'}), 401

if __name__ == "__main__":
    app.run(debug=True)