import os               #http://127.0.0.1:5000
import sys
import click
from flask import Flask,render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/home')
@app.route('/')
def index():
    user = User.quert.first()
    movies = Movie.query.all()
    return render_template('index.html',user = user,movies=movies)
@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name
@app.route('/test')
def test_url_for():
    print(url_for('hello'))     #url_for
    print(url_for('user_page',name='dengkw'))
    print(url_for('user_page', name='kiven'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'
@app.cli.command()
@click.option('--drop',is_flag=True,help='Create after frop.')
    # 设置选项
def initdb(drop):
    """Iiitialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')
@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    name = 'dengkw'
    movies = [
        {'title': 'My Neighbor Totoro', 'year':'1988'},
        {'title': 'Dead Poets Society', 'year':'1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('Done.')
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.String(20))
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))










    