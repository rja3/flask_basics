from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create the flask app instance
app = Flask(__name__)

# Python dictionary provided by Flash app
app.config.update(
    SECRET_KEY='secret-key',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:dog-bark3@localhost:5433/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)


# Create a database and pass the Flask app to it.
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World'


class Publication(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Publisher is {}.'.format(self.name)


class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, format, image, num_pages, pub_id):

        self.title = title
        self.author =   author
        self.avg_rating = avg_rating
        self.format = format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id


    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)

app.debug = True
db.create_all()

if __name__ == '__main__':

    # Run the flask app
    app.run(debug=True)
