from flask import Blueprint, render_template, Response, make_response, request,  flash, redirect, url_for
from flask_login import login_required, current_user
from ._scramblegen import *
from .cube import *
from .colourscanning import *
from .scramblemap import generate_scramble_map
from datetime import datetime, timedelta
from .models import User, Time
from . import db

start_time = False
elapsed_time = timedelta(seconds=0)

views = Blueprint('views', __name__)

#defining our view
@views.route('/')
@login_required
def home():
    #gets current user's name from User database
    name = User.query.get(current_user.id).username
    return render_template('home.html', user=current_user, name = name)
#reference the current user and check if they're authenticated

def stopwatch():
    global start_time, elapsed_time
    if request.method == "POST":
        if "start" in request.form:
            start_time = datetime.now()
            elapsed_time = timedelta(seconds=0)
            flash("Time is being recorded", category = 'primary')
        elif "stop" in request.form:
            if start_time:
                end_time = datetime.now()
                elapsed_time += end_time - start_time
                start_time = False
            else:
                pass
        elif "store" in request.form:
            if round(elapsed_time.total_seconds(), 2) >= 3.13:
                #turning it into a floating point value so that it can be uploaded into the database
                proper_time = round(elapsed_time.total_seconds(), 2)
                new_time = Time(data=proper_time, user_id = current_user.id)
                db.session.add(new_time)
                db.session.commit()
                flash('Time added!', category = 'success')
            else:
                flash('There is no way you are this fast, you better call Guinness because you just broke the world record.', category = 'error')
    else:
        pass
    return elapsed_time

@views.route('/Timer', methods=['GET', 'POST'])
def timer():
    global start_time, elapsed_time
    elapsed_time = stopwatch()
    longest_time = Time.query.filter_by(user_id=current_user.id) \
                       .order_by(Time.data.desc()) \
                       .first()
    shortest_time = Time.query.filter_by(user_id=current_user.id)\
                       .order_by(Time.data.asc()) \
                       .first()
    length = Time.query.filter_by(user_id=current_user.id).count()
    # print('length', length)

    #check if that user has any time values
    if longest_time and shortest_time:
        longest_time_value = longest_time.data
        shortest_time_value = shortest_time.data
    else:
        longest_time_value = 0
        shortest_time_value = 0

    #check to make sure user has at least 3 time values
    if length >= 3:
        sum = 0
        last_three_values = Time.query.filter_by(user_id=current_user.id) \
                            .order_by(Time.id.desc()) \
                            .limit(3) \
                            .all()
        for i in range(3):
            v = float(last_three_values[i].data)
            sum += v
        avg = float(sum/3)
        avg_of_3 = round(avg, 2)
    else:
        avg_of_3 = 0
    
    #checks to make sure user has at least 10 time values
    if length >= 10:
        ten =[]
        last_ten_values = Time.query.filter_by(user_id=current_user.id) \
                            .order_by(Time.id.desc()) \
                            .limit(10) \
                            .all()
        for i in range(10):
            ten.append(round(float(last_ten_values[i].data) , 2))
    else:
        ten =[]
        last_x_values = Time.query.filter_by(user_id=current_user.id) \
                            .order_by(Time.id.desc()) \
                            .limit(length) \
                            .all()
        for i in range(length):
            ten.append(round(float(last_x_values[i].data) , 2))
    return render_template("timer.html", user = current_user, scramble= stringscramble(current_scramble), elapsed_time = round(elapsed_time.total_seconds(), 2), longest_time = longest_time_value, shortest_time = shortest_time_value, a03 = avg_of_3, ten=ten)
    #return render_template('timer.html', user = current_user, scramble = stringscramble(y))

@views.route("/Scramble-Verification")
def Scramble_Verification(): 
    x = scramble(current_scramble)
    return render_template("scramble.html",  user = current_user, sc = stringscramble(current_scramble), cube = stringcube(x))
# sc = turning the scramble into a string to display onto the website, cube, we are scrambling the cube object

@views.route("/Map")
def Map():
   scramble_map = generate_scramble_map()
   retval, buffer = cv2.imencode('.png', scramble_map)
   response = make_response(buffer.tobytes())
   return response

@views.route("/Notation-Trainer",  methods=['GET', 'POST'])
def Notation():
    image = 'https://whitescreen.dev/images/pro/white-screen_32.png'
    if request.method == "POST":
        if "U" in request.form:
            image = "https://i.postimg.cc/wBcqrcbW/1.jpg"
        elif "D" in request.form:
            image = "https://i.postimg.cc/9MLWmX2Z/2.jpg"
        elif "R" in request.form:
            image = "https://i.postimg.cc/g0dd3Lk3/4.jpg"
        elif "L" in request.form:
            image = "https://i.postimg.cc/zDPJ4f01/3.jpg"
        elif "F" in request.form:
            image = "https://i.postimg.cc/mg7BcyRb/5.jpg"
        elif "B" in request.form:
            image = "https://i.postimg.cc/90SC9xrf/6.jpg"
        elif "M" in request.form:
            image = "https://i.postimg.cc/jdpRdkpg/7.jpg"
        elif "E" in request.form:
            image = "https://i.postimg.cc/ZKBTmhMv/8.jpg"
        elif "S" in request.form:
            image = "https://i.postimg.cc/MHXzvkZ4/9.jpg"
    return render_template('notation.html',  user = current_user, image = image)

@views.route("/S")
def S():
    return render_template('scanning.html', user=current_user)

@views.route("/Scanner")
def Scanner():
    # scanned_cube = return_scanned_cube()
    # correct = verifiying_scanned_cube(scanned_cube)
    #return render_template('scanning.html', user = current_user) #value = correct
    return Response(video_frame(text_scramble), mimetype='multipart/x-mixed-replace; boundary=frame')