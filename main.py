# ---------------------------- IMPORTED MODULES ------------------------------- #
import requests
import datetime
from requests.auth import HTTPBasicAuth

# ---------------------------- EXERCISE APP SECTION ------------------------------- #
EXERCISE_APP_ID = "a86c6134"
EXERCISE_API_KEY = "42ed7399bc4c4e08101902d33b12a802"

EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_headers = {
    "x-app-id": EXERCISE_APP_ID,
    "x-app-key": EXERCISE_API_KEY,
}

exercise_body = {
    "query": input("Какие физические упражнения сегодня ты сделал/a?: "),
    "gender": "male",
    "weight_kg": 94,
    "height_cm": 186,
    "age": 27,
}

exercise_respond = requests.post(url=EXERCISE_URL, json=exercise_body, headers=exercise_headers)
result = exercise_respond.json()
# ---------------------------- WORKING WITH GOOGLE SHEET APP ------------------------------- #
sheet_url = "https://api.sheety.co/c1941eafc77ece7d14cdfcb3121fd0c9/workouts/workouts"
today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")
sheet_inputs = {}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
print(sheet_inputs)
sheet_response = requests.post(url=sheet_url, json=sheet_inputs)
print(sheet_response.status_code)

# ---------------------------- END OF FILE ------------------------------- #
# response_for_print = requests.get(url="https://api.sheety.co/c1941eafc77ece7d14cdfcb3121fd0c9/myWorkouts/workouts")
# print(response_for_print.json())
# bearer_headers = {
#     "Authorization": f"Basic a2VtYWw6Unp2ZmticjE="
#     }
# sheet_response = requests.post(sheet_url, json=sheet_inputs, headers=bearer_headers)
# print(sheet_response.text)
