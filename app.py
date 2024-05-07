from flask import Flask, render_template, request, redirect, url_for, make_response
#import mysql.connector
import datetime
import matplotlib.pyplot as plt
import os

# instantiate the app
app = Flask(__name__)

# Connect to the database
# Insert code to connect to zoo database


#mydb = mysql.connector.connect(
    #host = "localhost",
    #user = "root",
    #password= "dap123",
    #database = "zoo"
#)

categories={'Guest Information':'guest','Room Information':'room','Reservation & Events':'reservation', 'Finance Statement':'finance'}

# set up the routes
@app.route('/')
def home():
    # Get today's date
    d = datetime.datetime.now()
    date_string = f'{d.month}/{d.day}/{d.year}'


    general_information = {'guest':51, 'room':'46%', 'reservation':11, 'revenue':'$5000'}
    # Link to the home page.

    return render_template('index.html', date=date_string,data=general_information, categories=categories)


@app.route('/guest')
def guest():
    # Get today's date
    d = datetime.datetime.now()
    date_string = f'{d.month}/{d.day}/{d.year}'

    # chart
    if not os.path.exists('static/images'):
        os.mkdir('static/images')

        # Path for the image
    img_path = 'static/images/guest_chart.png'

    # Create a plot
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])  # Example data
    plt.savefig(img_path)
    plt.close(fig)  # Close the figure to free up memory





    # Do query
    #cursor = mydb.cursor()
    #query = "select count roomId from room"
    #cursor.execute(query)
    #total_rooms = cursor.fetchall()

    # Example guest_information
    guest_information = {'total':51,'arrived':31,'leaving':20}
    # Link to the schedule page.  Pass the date as a parameter
    return render_template('guest.html', date = date_string, data= guest_information, image_file=img_path, categories=categories
                           )


@app.route('/room')
def room():
    # Get today's date
    d = datetime.datetime.now()
    date_string = f'{d.month}/{d.day}/{d.year}'

    # Do query
    #cursor = mydb.cursor()
    #query = "select count roomId from room"
    #cursor.execute(query)
    #total_rooms = cursor.fetchall()

    # Example room_information
    room_information = {'total':100,'available':50,'cleaning':3,'sleeping':'31/50','meeting':'12/40','suit':'4/10'}
    # Link to the schedule page.  Pass the date as a parameter
    return render_template('room.html', date = date_string, data= room_information, categories=categories
                           )

@app.route('/reservation')
def reservation():
    # Get today's date
    d = datetime.datetime.now()
    date_string = f'{d.month}/{d.day}/{d.year}'

    # Do query
    #cursor = mydb.cursor()
    #query = "select count roomId from room"
    #cursor.execute(query)
    #total_rooms = cursor.fetchall()

    #  Example information
    reservation_information = {'total':11,'tomorrow':3}
    event_information={'this':6,'next':2}
    event_today = {"Jeffrey's Wedding Ceremony":'18:00',"Joe's Party":'20:00'}
    # Link to the schedule page.  Pass the date as a parameter
    return render_template('reservation.html', date = date_string, res_data= reservation_information, event_detail = event_today, event_data=event_information, categories=categories
                           )

@app.route('/finance')
def finance():
    # Get today's date
    d = datetime.datetime.now()
    date_string = f'{d.month}/{d.day}/{d.year}'

    # Do query
    #cursor = mydb.cursor()
    #query = "select count roomId from room"
    #cursor.execute(query)
    #total_rooms = cursor.fetchall()

    #  Example information
    revenue_information = {'today':'$400','week':'$5000','month':'$8000'}
    room_revenue={'sleeping':'$2000','meeting':'$2000','suit':'$1000'}
    other = {"service":'$3000',"party":'Sam'}
    # Link to the schedule page.  Pass the date as a parameter
    return render_template('finance.html', date = date_string, rev_data= revenue_information, room_detail = room_revenue, other_data=other, categories=categories
                           )

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template

if __name__ == "__main__":
    app.run(debug = True)
