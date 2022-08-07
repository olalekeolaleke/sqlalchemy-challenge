from datetime import date
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
#Station = Base.classes.station
Measurement = Base.classes.measurement
Station = Base.classes.station

  # Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the Honolulu, Hawaii Climate Analysis and Exploration<br/>"
        f"Available Routes are:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start> (add start date)<br/>"
        f"/api/v1.0/<start>/<end> (add start & end date)<br/>"
    
    )   

@app.route("/api/v1.0/precipitation")
def precipitation():
# Previous Year 
    prv_year = "2016-08-23"

    """Return a JSON list of all precipitation from the dataset"""
    # Query all pprecipitation
    prcp_data = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prv_year).order_by(Measurement.date).all()
    

   # Create a dictionary from the row data and append to a list of all_precipitation
    all_precipitation = {"date":[],
                          "prcp":[] }
    for date, prcp in prcp_data:
    
        all_precipitation["date"].append(date)
        all_precipitation["prcp"].append(prcp)
        


    print(all_precipitation)
    


    return jsonify(all_precipitation)


"""Return a JSON list of all stations from the dataset"""

@app.route("/api/v1.0/stations")
def station():
    station_data = session.query(Station.station, Station.name).all()
    stations = list(np.ravel(station_data))
    print(stations)
    return jsonify(stations)


"""Return a JSON list of all temperature observations (TOBS) for the previous year"""

@app.route("/api/v1.0/tobs")
def tobs():
    prv_year = "2016-08-23"
    tobs_data = session.query(Measurement.tobs).\
        filter(Measurement.station=='USC00519281').\
        filter(Measurement.date >= prv_year).all()

    tobs = list(np.ravel(tobs_data))
    print(tobs)
    return jsonify(tobs)

"""Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a start range """

@app.route("/api/v1.0/<start>")
def startDate(start):

    start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    end =  dt.date(2016, 12, 31)
    startdate_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    startdate = list(np.ravel(startdate_data))
    print(startdate)
    return jsonify(startdate)

"""Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for start-end range"""  

@app.route("/api/v1.0/<start>/<end>")
def StartDateEndDate(start,end):
    start_date= dt.datetime.strptime(start, '%Y-%m-%d')
    end_date = dt.datetime.strptime(end, '%Y-%m-%d')
    end =  dt.date(2016, 12, 31)
    start = dt.date(2015, 1, 1)
    
    startdate_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    startdate = list(np.ravel(startdate_data))
    print(startdate)
    return jsonify(startdate)



session.close

if __name__ == '__main__':
        app.run(debug=True)





