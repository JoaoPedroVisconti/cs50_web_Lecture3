import os

from config import DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import  scoped_session, sessionmaker

engine = create_engine(DATABASE_URI)
db = scoped_session(sessionmaker(bind=engine))

def main():
    
    #List of all flights
    flights = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"Flight {flight.id}: {flight.origin} to {flight.destination}, {flight.duration} minutes")
    
    
    # Prompt user to choose a flight    
    flight_id = int(input("\nFlight ID: "))
    flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id = :id",
                        {"id":flight_id}).fetchone()
    
    # Make sure flight is valid.
    if flight is None:
        print("Error: no such flight")
        return
    
    # List of passengers
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                            {"flight_id": flight_id}).fetchall()
    
    print("\nPasssengers: ")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == 0:
        print("No passengers")
        
    # db.commit()
        
if __name__ == "__main__":
    main()