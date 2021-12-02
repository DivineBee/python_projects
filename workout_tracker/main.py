import requests
from datetime import datetime
import os
APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
BEARER_TOKEN_AUTH = os.environ['BEARER_TOKEN_AUTH']

sheety_endpoint = os.environ['sheety_endpoint']

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_type = input("Which exercise you did?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

post_exercises_params = {
    "query": exercise_type,
    "gender": "female",
    "weight_kg": 47,
    "height_cm": 158,
    "age": 22
}

result = requests.post(url=exercise_endpoint, json=post_exercises_params, headers=headers)
result = result.json()

today = datetime.now().strftime("%x")
time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    headers_auth = {
        "Authorization": BEARER_TOKEN_AUTH
    }

    workout_data = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    post_workout = requests.post(url=sheety_endpoint, json=workout_data, headers=headers_auth)

    print(post_workout.text)