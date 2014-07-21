from flask import Flask, session, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def index():
	if 'login' in session:
		return 'hello %s' % session['login']
	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['login'] = request.form['login']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=login>
            <p><input type=submit value=Login>
        </form>
        '''

@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('index'))

app.secret_key = 'YouDontKnowMySecret'

if __name__ == "__main__":
    app.run(debug=True)