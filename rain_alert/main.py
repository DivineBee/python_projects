import requests
from twilio.rest import Client

api_key = "" # api_key = os.environ.get("OWM_API_KEY")
weather_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = ""
auth_token = ""

from_tel = ""
to_tel = ""
MY_LAT = 2
MY_LONG = 2

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(weather_endpoint, params=parameters)
response.raise_for_status()
hourly_weather = []
will_rain = False

for i in range(0, 12):
    code = response.json()["hourly"][i]["weather"][0]["id"]
    hourly_weather.append(code)
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will rain today!",
        from_=from_tel,
        to=to_tel
    )
# # Alternative solution
# will_rain = False
#
# weather_data = response.json()["hourly"][:12]
# for hour_data in weather_data:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True
#
# if will_rain:
#     print("Bring an umbrella")
