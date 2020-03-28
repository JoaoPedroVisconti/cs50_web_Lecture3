from flask import Flask, render_template, request

from config import DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import  scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(DATABASE_URI)
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight"""
    
    #Get information
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid number")
    
    # Make sure that the flight exsist
    if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No flight with that ID")
    
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)", 
               {"name": name, "flight_id": flight_id})
    db.commit()
    return render_template("success.html")

@app.route("/flights")
def flihgts():
    """list of flights"""
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """Lists details about a single flight"""
    
    # Make sure that the flight exsist
    flight = db.execute("SELECT * FROM flights WHERE id= :id", {"id": flight_id }).fetchone()
    if flight is None:
        return render_template("error.html", message="No flight")
    
    # Get all passengers
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                            {"flight_id": flight_id}).fetchall()
    
    return render_template("flight.html", flight=flight, passengers=passengers)