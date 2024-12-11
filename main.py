import requests
from datetime import datetime
import os

WEIGHT_KG = 80
HEIGHT_CM = 182
AGE = 31


APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
url = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
    "query": input("Tell me which exercise you did: "),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=url, json=params, headers=headers)
result = response.json()

AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
SHEETY_API = os.environ.get("SHEETY_API")

sheety_headers = {
    "Authorization": AUTH_TOKEN
}
today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_hour = today.strftime("%X")
exercises_list = result['exercises']
for exercise in exercises_list:
    sheety_params = {
        "workout": {
            "date": today_date,
            "time": today_hour,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    sheety_url = f"https://api.sheety.co/{SHEETY_API}/workoutTracking/workouts"
    sheety_response = requests.post(url=sheety_url, json=sheety_params, headers=sheety_headers)
    print(sheety_response.json())
