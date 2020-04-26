from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# set up session
engine=create_engine('sqlite:///hawaii.sqlite')
Base=automap_base()
Base.prepare(engine, reflect=True)
Measurement=Base.classes.measurement
Station=Base.classes.station
session=Session(engine)

# set up Flask
app=Flask(__name__)

@app.route('/')
def welcome(): 
    return('hi')

@app.route('/api/v1.0/precipitation')
def precipitation():
    results=session.query(Measurement.date, Measurement.prcp)
    precipitation={date: prcp for date, prcp in results}
    return jsonify(precipitation)

@app.route('/api/v1.0/stations')
def stations():
    return('stations')

if __name__=='__main__':
    app.run()