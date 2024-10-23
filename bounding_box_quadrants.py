import math
import csv

# Define the bounding box for Greater Tampa Bay
bounding_box = {
    "north": 28.1900,  # Northernmost latitude
    "south": 27.6400,  # Southernmost latitude
    "west": -82.8300,  # Westernmost longitude
    "east": -82.2200   # Easternmost longitude
}

# Function to create quadrants
def create_quadrants(bounding_box, step_lat=0.0145, step_lon=0.0145):
    lat_range = abs(bounding_box["north"] - bounding_box["south"])
    lon_range = abs(bounding_box["west"] - bounding_box["east"])
    
    lat_steps = math.ceil(lat_range / step_lat)
    lon_steps = math.ceil(lon_range / step_lon)
    
    quadrants = []
    
    for i in range(lat_steps):
        for j in range(lon_steps):
            north = bounding_box["north"] - i * step_lat
            south = north - step_lat
            west = bounding_box["west"] + j * step_lon
            east = west + step_lon
            
            quadrant = {
                "id": f"Q{i+1}{chr(65+j)}",
                "north": north,
                "south": south,
                "west": west,
                "east": east
            }
            quadrants.append(quadrant)
    
    return quadrants

# Generate the quadrants
quadrants = create_quadrants(bounding_box)

# Save the quadrants to a CSV file
with open('quadrants.csv', 'w', newline='') as csvfile:
    fieldnames = ['Quadrant ID', 'North', 'South', 'West', 'East']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for quadrant in quadrants:
        writer.writerow({
            'Quadrant ID': quadrant['id'],
            'North': quadrant['north'],
            'South': quadrant['south'],
            'West': quadrant['west'],
            'East': quadrant['east']
        })

print(f"Quadrant data saved to 'quadrants.csv'.")
