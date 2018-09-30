from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello, world!'

@app.route('/bye')
def bye():
	return 'Bye everyone.'

if __name__ == '__main__':
    app.run(debug=True)