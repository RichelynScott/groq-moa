import requests
import pandas as pd
import csv

# Your Google Places API key
API_KEY = 'AIzaSyA2qQsK9WvYz1gWuYkGhki3HNd99meZn4U'

# Load the quadrants data with the correct path
quadrants = pd.read_csv('/Users/richelynscott/GPT_ENVs/groq-moa/quadrants.csv')

# Function to fetch business data using the 'establishment' type
def fetch_business_data(quadrant):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': f"{(quadrant['North'] + quadrant['South']) / 2},{(quadrant['West'] + quadrant['East']) / 2}",
        'radius': 1500,  # Approx 1 mile radius
        'type': 'establishment',  # Broad type of place
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    print(f"API Response for Quadrant {quadrant['Quadrant ID']}: {response.json()}")  # Print the raw API response for debugging
    return response.json()

# Fetch and save business data for each quadrant
with open('/Users/richelynscott/GPT_ENVs/groq-moa/business_data_debug.csv', 'w', newline='') as csvfile:
    fieldnames = ['Quadrant ID', 'Business Name', 'Address', 'Latitude', 'Longitude', 'Place ID']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for _, quadrant in quadrants.iterrows():
        business_data = fetch_business_data(quadrant)
        if 'results' in business_data:
            for place in business_data['results']:
                writer.writerow({
                    'Quadrant ID': quadrant['Quadrant ID'],
                    'Business Name': place.get('name'),
                    'Address': place.get('formatted_address'),
                    'Latitude': place.get('geometry', {}).get('location', {}).get('lat'),
                    'Longitude': place.get('geometry', {}).get('location', {}).get('lng'),
                    'Place ID': place.get('place_id')
                })

print("Business data has been saved to 'business_data_debug.csv' with debug information.")