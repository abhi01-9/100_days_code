import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "OWM_API"
account_sid = "Twilio accound sid"
auth_token = "Auth token of twilio"

weather_params = {
    "lat": 27.228498,
    "lon": 79.024956,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()["list"]
will_rain = False
for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrealla",
        from_="+23525246",
        to="+912342352"
    )
    print(message.status)
