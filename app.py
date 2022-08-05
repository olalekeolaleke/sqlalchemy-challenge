import numpy as np
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
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    
    )   

@app.route("/api/v1.0/precipitation")
def precipitation():
# Previous Year 
    prv_year = "2016-08-23"

    """Return a list of all precipitation """
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


@app.route("/api/v1.0/stations")
def station():
    station_data = session.query(Station.station, Station.name).all()
    stations = list(np.ravel(station_data))
    print(stations)
    return jsonify(stations)

@app.route("/api/v1.0/tobs")

def tobs():
    prv_year = "2016-08-23"
    tobs_data = session.query(Measurement.tobs).\
        filter(Measurement.station=='USC00519281').\
        filter(Measurement.date >= prv_year).all()

    tobs = list(np.ravel(tobs_data))
    print(tobs)
    return jsonify(tobs)


@app.route("/api/v1.0/<start>")
def StartDateOnly():
    startdate_data = session.query()





session.close

if __name__ == '__main__':
        app.run(debug=True)





