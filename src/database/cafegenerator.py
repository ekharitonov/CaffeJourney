import pandas as pd
import random

# Harrisburg coordinates
harrisburg_lat = 40.2732
harrisburg_lon = -76.8867

# Function to generate random coordinates within a 30-mile radius
def random_coordinates(lat, lon, radius=30):
    # Convert radius from miles to degrees (approximation)
    radius_in_degrees = radius / 69.0

    # Generate random latitude and longitude
    random_lat = lat + random.uniform(-radius_in_degrees, radius_in_degrees)
    random_lon = lon + random.uniform(-radius_in_degrees, radius_in_degrees)
    return random_lat, random_lon

# Sample data for randomization
cafe_names = ["Cafe Harmony", "Bean Bliss", "Mocha Magic", "Espresso Express", "Latte Lounge"]
addresses = ["Main St", "Elm St", "Maple Ave", "Oak St", "Pine St"]

# Function to generate random cafes
def generate_cafes(num_cafes):
    cafes = []
    for i in range(1, num_cafes + 1):
        name = random.choice(cafe_names) + " " + str(random.randint(1, 100))
        address = str(random.randint(100, 999)) + " " + random.choice(addresses)
        price = round(random.uniform(2.0, 15.0), 2)  # Random price between 2 and 15
        lat, lon = random_coordinates(harrisburg_lat, harrisburg_lon)
        cafes.append([i, name, address, price, lat, lon])
    return cafes

# Generate data for a specified number of cafes
num_cafes = 10  # Change this number to generate more or fewer cafes
cafe_data = generate_cafes(num_cafes)

# Create a DataFrame and save to a .txt file
df = pd.DataFrame(cafe_data, columns=["NUM", "NAME", "ADDRESS", "PRICE", "LAT", "LON"])
df.to_csv("pubs.txt", index=False)
