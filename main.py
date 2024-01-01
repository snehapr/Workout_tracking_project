# ------Nutritionix API ---------------
import datetime as datetime
import requests
import datetime

APP_ID = "****4r9**"
API_KEY = "******************3a97ea***"


API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

api_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

input_query = input("Tell me which exercise you did: ")

api_data = {
 "query": input_query
}


exercise_request = requests.post(url=API_ENDPOINT, headers=api_headers, data=api_data)
# print(exercise_request.text)


exercise_request_json = exercise_request.json()
# print(exercise_request_json)

exercises = exercise_request_json["exercises"]
print(exercises)

exercise_name = []
duration_min = []
calories_burnt = []

for no in exercises:
    name = no["user_input"]
    exercise_name.append(name)
    minutes = no["duration_min"]
    duration_min.append(minutes)
    calories = no["nf_calories"]
    calories_burnt.append(calories)

print(exercise_name)
print(duration_min)
print(calories_burnt)




# ------- Adding the row in the google sheet using the sheety------

SHEETY_API_ENDPOINT = "https://api.sheety.co/*******f5f44ea4807165f9d0e0****/workoutsTracking/workouts"


def fetch_time():
    time_now = datetime.datetime.now()
    time_now = time_now.strftime("%X")
    return time_now


def fetch_date():
    date_now = datetime.datetime.now()
    date_now = date_now.strftime("%d/%m/%Y")
    return date_now


def fetch_exercise(exercise_index):
    return exercise_name[exercise_index]


def fetch_duration(exercise_index):
    return duration_min[exercise_index]


def fetch_calories(exercise_index):
    return calories_burnt[exercise_index]


no_of_records = len(exercise_name)

auth_headers ={
    "Authorization": "Basic c25laGFfc********************=="
}

for no_rows in range(0, no_of_records):
    sheety_body = {
        "workout": {
            "date": fetch_date(),
            "time": fetch_time(),
            "exercise": fetch_exercise(no_rows),
            "duration": fetch_duration(no_rows),
            "calories": fetch_calories(no_rows),
        }
    }
    sheety_request = requests.post(url=SHEETY_API_ENDPOINT, headers=auth_headers, json=sheety_body)
    print(sheety_request.text)







