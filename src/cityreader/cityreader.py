# Importing built-in csv module to read data in cities.csv file 
import csv 

# Class City holds name, lat and lon 
class City():
  def __init__(self, name, lat, lon): 
    self.name = name 
    self.lat = float(lat) # Converting to float because csv data has decimals 
    self.lon = float(lon)


  ## Setting up to be printed 
  def __str__(self): 
     return f"{self.name}: {self.lat}, {self.lon}"

# Empty cities list for storing cities 
cities = []

def cityreader(cities=[]):
  
  # Functionality to open and read from the 'cities.csv' file
  with open("cities.csv", newline="") as csvfile: 
    reader = csv.DictReader(csvfile)

    # For each city record, create a new City instance and add it to the cities` list
    for row in reader: 
      cities.append(City(row["city"], row["lat"], row["lng"])) # Tricky that lng is in the csv, not lon
    
    # Return the list with all the City instances from the function.
    return cities

# Execute the function so data populates 
cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []

  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  return within
