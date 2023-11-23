from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


# Define the form for adding a new cafe
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[validators.DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)',
                           validators=[validators.DataRequired(), validators.URL()])
    open_time = StringField('Opening Time e.g. 8AM', validators=[validators.DataRequired()])
    closing_time = StringField('Closing Time e.g. 5:30PM', validators=[validators.DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'],
                                validators=[validators.DataRequired()])
    wifi_rating = SelectField('Wi-Fi Strength Rating', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
                              validators=[validators.DataRequired()])
    power_socket = SelectField('Power Socket Availability', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
                               validators=[validators.DataRequired()])
    submit = SubmitField('Submit')


# Define the home route
@app.route("/")
def home():
    return render_template("index.html")


# Define the route for adding a new cafe
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        # Get data from the form
        cafe_name = form.cafe.data
        location = form.location.data
        open_time = form.open_time.data
        close_time = form.closing_time.data
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.wifi_rating.data
        power_socket = form.power_socket.data

        # Append the data to the CSV file
        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([cafe_name, location, open_time, close_time, coffee_rating, wifi_rating, power_socket])

        # Redirect to the 'cafes' route
        return redirect(url_for('cafes'))

    # Render the 'add.html' template with the form
    return render_template('add.html', form=form)


# Define the 'cafes' route
@app.route('/cafes')
def cafes():
    # Read data from the CSV file and store it in a list
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    # Render the 'cafes.html' template with the data
    return render_template('cafes.html', cafes=list_of_rows)


# Run the Flask app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
