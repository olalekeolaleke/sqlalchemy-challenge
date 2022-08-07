# sql alchemy-challenge

This challenge focuses on the climate analysis of my next holiday destination. I have 
decided to treat myself to a long holiday vacation in Honolulu, Hawaii and planning 
for the trip, I have decided to do somme climate analysis of the area.

This challenge has been grouped into the two major part.

The first part being, Climate Analysis and Exploration

This part was decided into two parts which is the Precipitation and Station analysis

Under the Precipitation analysis, previous 12 months of precipitation data was retrieved by querying 
the 12 previous months of data using the most recent date in a dataset.

The date and prcp values were only selected from the output and then loaded into a Pandas 
DataFrame, and the date column was set as the index.

The results were plotted and summary statistics for the precipitation data were calculated
using Pandas DataFrame

While under the Station analysis part, a query was design to calculate the total number of
 stations in the dataset and the most active stations
 
The list of stations and observation counts were retrieve and a query was designed to retrieve 
the station id that has the highest number of observations.

A query was also designed the previous 12 months of temperature observation data (TOBS)
for this station and a histogram was plotted using the results with bins=12

The Second part of this challenge is the Temperature Analysis

Under this part, the calc_temps function twas used o calculate the minimum, average, and 
maximum temperatures for the trip using the matching dates from a previous year

The results were then used to plot a bar chart.

The total amount of rainfall per weather station for your trip dates using the previous year's 
matching dates and the daily normals were calculated 

The daily normals output were loaded into a Pandas DataFrame and was plotted as an area 
plot with (stacked=False) using Pandas DataFrame
 


