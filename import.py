import csv
import os

from config import DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import  scoped_session, sessionmaker

engine = create_engine(DATABASE_URI)
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("C:/Users/Joao/EngenhariaGoogleDrive/Development/Courses/CS50/WebDevelopment/cs50_web_Lecture3/flights.csv")
    reader = csv.reader(f)
    
    for orig, dest, dur in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                   {"origin": orig, "destination": dest, "duration":dur})

        print(f"Added flight from {orig} to {dest} lasting {dur}")
    
    db.commit()
    
if __name__ == "__main__":
    main()