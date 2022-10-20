from flask import Flask, Blueprint, redirect, render_template, url_for, request, flash
import os
import requests
import json
from dotenv import load_dotenv
from config import Config
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from findpokemon import Pokemon, findPokeByName
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')

app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ykbabspm:zgFdiuKnJFNRWMNQsAVw1WE1W8cqi5OF@peanut.db.elephantsql.com/ykbabspm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)



class User_Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow())
    
    
    def __init__(self, name, date_added):
        self.name = name
        self.date_added = date_added
        


@app.route("/")
def index():
    return render_template('home.html')


@app.route(f"/pokemon", methods=["POST", "GET"])
def pokemon():
    if request.method == 'POST':
        pokeName = request.form.get('pokemon')
        pokeName = pokeName.capitalize()
        pokemon = findPokeByName(pokeName)
        
            
        db.session.add(pokemon)
        db.session.commit()
        
    else:
        return render_template('error.html')

    return render_template('pokemon.html', 
        pokemon=pokemon
        )


@app.route("/error")
def error():
    return render_template('error.html')



if __name__ == '__main__':
    app.run(debug=True)



    

