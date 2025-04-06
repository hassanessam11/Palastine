from flask import Flask, render_template, request, redirect, url_for, session, flash
from Palastine import app
from Palastine.models import User, db
import requests
import json
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/messages',methods=['GET', 'POST'])
def messages():

    return render_template('messege.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form.get('message')
    if message:
        req=requests.get('https://geolocation-db.com/json').json()
        print(req)
        # Here you would typically process the message, e.g., save it to a database or send it to an API
        message=User(message=message,
                     country=req.get('country_name'),
                     ip_address=req.get('IPv4'))
        db.session.add(message)
        db.session.commit()
        flash('Message sent successfully!', 'success')
    else:
        flash('Message cannot be empty.', 'error')
    return redirect(url_for('home'))

# EAAYQrgvlCZCEBO1hCsqeVmZBWS5V6L4uSvpwNKBqli9cZBI97XsdipwZB6MlMq4m7L8hAVWYwPiPA9jiLtsmLpd3GF5EjCl9UtbNdCKWnOVggxXQZA8997038RhaGzkfZCi5q6G71051rnrZBzQc85o6euTZBdJw8lbFV7BF0WYxhuZASlvZA9HnLGySzIt3oP8CInZAAZDZD





@app.route('/get-message', methods=['GET'])
def get_message():
    unsent_user = User.query.filter_by(sent=False).order_by(User.created_at.asc()).first()
    
    if unsent_user:
        message = unsent_user.message
        unsent_user.sent = True  # تحديث حالة الإرسال
        db.session.commit()
    else:
        message = "لا توجد رسائل غير مُرسلة حالياً."
    
    return json.dumps({"message": message, "number": ""}), 200, {'Content-Type': 'application/json'}
