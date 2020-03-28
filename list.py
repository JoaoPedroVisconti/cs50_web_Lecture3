import os
from config import DATABASE_URI

from sqlalchemy import create_engine
from sqlalchemy.orm import  scoped_session, sessionmaker

engine = create_engine(DATABASE_URI)
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} min")
        
if __name__ == "__main__":
    main()