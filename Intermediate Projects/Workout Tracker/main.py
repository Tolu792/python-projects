import requests
from datetime import datetime
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/1d750bcd7a604b38e04714a6d8ed906e/workoutTracking/workouts"
exercise_input = input("Tell me which exercises you did?: ")

GENDER = "male"
WEIGHT = 55.5
HEIGHT = 166
AGE = 20

headers = {
    "x-app-id": os.getenv('APP_ID'),
    "x-app-key": os.getenv('API_KEY'),
}

sheety_header = {
    "Authorization": os.getenv('TOKEN'),
}

data = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=data, headers=headers)
response.raise_for_status()
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    exercise_data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, headers=sheety_header, json=exercise_data)
    sheety_response.raise_for_status()
    print(sheety_response.text)
