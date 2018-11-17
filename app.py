from flask import Flask, render_template

app = Flask(__name__)

@app.route('/homepage')
def home():
	"""
    return homepage
	"""
	title = "Jamii"
	return render_template('app.html', name=title)

if __name__ == '__main__':
	app.run(debug=True)