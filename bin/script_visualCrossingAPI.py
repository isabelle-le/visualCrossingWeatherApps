import requests as req
import json


def weather_api_call(requestURL, parameters):
    response = req.get(url=requestURL, params=parameters)
    if response.status_code != 200:
        print(response.json())
        exit()
    data = response.json()
    return json.dumps(data)


def get_single_weather(key, unitgroup="metric", contenttype='json'):
    requestURL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Paris?"
    parameters = {"key": key, "unitGroup": unitgroup,"contentType":contenttype}
    return weather_api_call(requestURL, parameters)
print('')
print(' - Requesting weather : ')

def main():
    key = "QRLSXGZEPLWWUC7JLBEQAVQSE"
    upcoming_movie_list = get_single_weather(key, "metric","json")
    data = json.loads(upcoming_movie_list)
    print(json.dumps(data["days"]))

if __name__ == "__main__":
    main()
