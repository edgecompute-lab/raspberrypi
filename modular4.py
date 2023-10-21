import pyrebase
from distance import distance
import time

# Initialize Firebase connection and return the database object
def initialize_firebase():
    # Firebase configuration parameters
    config = {
  "apiKey": "AIzaSyC_77TtgK9aL4xR2SqQvy1YURc7opOmUzs",
  "authDomain": "ultrasound1-682d9.firebaseapp.com",
  "databaseURL": "https://ultrasound1-682d9-default-rtdb.firebaseio.com",
  "projectId": "ultrasound1-682d9",
  "storageBucket": "ultrasound1-682d9.appspot.com",
  "messagingSenderId": "192519938023",
  "appId": "1:192519938023:web:546e5150e9549389b16742"
    }

    # Initialize Firebase app and get the database instance
    firebase = pyrebase.initialize_app(config)
    return firebase.database()

# Generate a timestamp with day, hour, minute, and second
def get_current_timestamp():
    # Get the current time in local time
    current_time = time.localtime()
    
    # Format the timestamp as "date:day,Hr:hour,Min:minute,Sec:second"
    formatted_timestamp = f"date:{current_time.tm_mday},Hr:{current_time.tm_hour},Min:{current_time.tm_min},Sec:{current_time.tm_sec}"
    return formatted_timestamp

# Store the distance reading in the Firebase database
def store_distance_reading(database, key, value):
    # Create a data dictionary with the timestamp as the key and the distance value
    data = {key: value}
    
    # Update the Firebase database with the data
    database.child("DB object name").update(data)

# Read the distance value and print it
def read_distance_and_print():
    # Call the 'distance' function to get the distance reading
    distance_value = distance()
    
    # Print the distance value to the console
    print(distance_value)
    
    return distance_value

# Main function to run the program
def main():
    # Initialize the Firebase database connection
    database = initialize_firebase()

    while True:
        # Read the distance value and print it
        distance_value = read_distance_and_print()

        # Generate a timestamp
        timestamp = get_current_timestamp()

        # Store the distance reading in the Firebase database
        store_distance_reading(database, timestamp, distance_value)

        # Sleep for 15 seconds before the next reading
        time.sleep(15)

if __name__ == "__main__":
    main()
