from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, validators
import requests

# CONSTANTS
DATABASE_URL = "https://api.themoviedb.org/3/search/movie"
AUTHORIZATION = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkMmRlY2NlZWEzZTgyMzkzMDIyZTYyZDc0OGZlMTdjMyIsInN1YiI6IjY1Mjg3ZDFkMGNiMzM1MTZmODgxZjcyNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.L0rWPxkiQgCpPXk3Y1GbLqPgcb5eV06MvR2jG4kVUew"
IMAGE_URL = "https://image.tmdb.org/t/p/w780"
HEADERS = {
    "accept": "application/json",
    "Authorization": AUTHORIZATION,
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-10-movies.db"
db = SQLAlchemy(app)
Bootstrap(app)


# Define the form for adding a movie
class AddMovie(FlaskForm):
    movie_title = StringField('Movie Title', validators=[validators.DataRequired()])
    submit = SubmitField('Add Movie')


# Define the form for editing a movie
class EditMovie(FlaskForm):
    rating = FloatField('Your Rating Out of 10 e.g. 7.5', validators=[validators.DataRequired()])
    review = StringField('Your Review', validators=[validators.DataRequired()])
    submit = SubmitField('Done')


# Define the "Movie" model for the database
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True, default=0.0)
    ranking = db.Column(db.Integer, nullable=True, default="None")
    review = db.Column(db.String(250), nullable=True, default="None")
    img_url = db.Column(db.String(250), nullable=False)


# Create the database tables
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()

    for movie in range(len(all_movies)):
        all_movies[movie].ranking = len(all_movies) - movie
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        movie_title = form.movie_title.data
        response = requests.get(url=DATABASE_URL, headers=HEADERS, params={"query": movie_title})
        response.raise_for_status()
        data = response.json()["results"]
        return render_template('select.html', options=data)
    return render_template('add.html', form=form)


@app.route('/find')
def find_movie():
    movie_id = request.args.get('id')
    if movie_id:
        url = f"{DATABASE_URL}/{movie_id}"
        response = requests.get(url=url, headers=HEADERS)
        data = response.json()

        new_movie = Movie(
            title=data['title'],
            year=data['release_date'].split('-')[0],
            description=data['overview'],
            img_url=IMAGE_URL + data['poster_path']
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for('edit', id=new_movie.id))


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditMovie()
    movie_id = request.args.get('id')
    movie_to_update = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_to_update.rating = form.rating.data
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie_to_update)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
