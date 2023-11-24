from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)


# Define the "Books" model for the database
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# Create the database tables
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # Read All Records
    all_books = db.session.query(Books).all()

    return render_template('index.html', books=all_books)


@app.route('/delete')
def delete():
    # Get the book ID from the request
    book_id = request.args.get('id')
    # Query the database to get the book to delete
    book_to_delete = Books.query.get(book_id)
    # Delete the book from the database
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        # Create a new book instance with data from the form
        book = Books(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        # Add the new instance to the session
        db.session.add(book)
        # Commit the changes to the database
        db.session.commit()
        # Redirect to the home page
        return redirect(url_for('home'))
    # Render the "add.html" template for adding a new book
    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == "POST":
        # Get the book ID and the new rating from the form
        book_id = request.form["id"]
        # Query the database to get the book to update
        book_to_update = Books.query.get(book_id)
        # Update the book's rating
        book_to_update.rating = request.form["rating"]
        # Commit the changes to the database
        db.session.commit()
        # Redirect to the home page
        return redirect(url_for('home'))
    # Get the book ID from the URL parameters
    book_id = request.args.get('id')
    # Query the database to get the book for editing
    requested_book = Books.query.get(book_id)
    # Render the "edit.html" template with the book data
    return render_template('edit.html', book=requested_book)


if __name__ == '__main__':
    app.run(debug=True)
