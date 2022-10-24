from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLACLHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User: ' + name + '-' + str(id)

if __name__ == '__main__':
    app.run(debug=True)