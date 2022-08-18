import requests as req
import urllib
import json


def weather_api_call(requestURL, parameters):
    response = req.get(url=requestURL, params=parameters)
    print(response.url)
    if response.status_code != 200:
        print(response.json())
        exit()
    data = response.json()
    return json.dumps(data)



def get_single_weather(key, unit_group="metric",elements="datetime,datetimeEpoch,name,address,resolvedAddress,latitude,longitude,temp,humidity,precip,solarradiation,solarenergy,stations,source", include = "obs", content_type="json"):
    """
    :param key: api_key QRLSXGZEPLWWUC7JLBEQAVQSE
    :param unit_group: metric °c,km
    :param max_distance(meters): max=200km or 200000m
    :param elements: values
    :param include: obs: station observation, remote: remote observation satellite/radar, fcst: forecast,Cobs: combination
    :param content_type:json
    :return:weather_api_call
    """
    requestURL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" + urllib.parse.quote("LFPO") +"/"+ urllib.parse.quote("today")
    parameters = {"key": key,"unitGroup": unit_group,"elements" : elements, "include" : include,"contentType":content_type}
    return weather_api_call(requestURL, parameters)
print('')
print(' - Requesting weather : ')


def main():
    key = "QRLSXGZEPLWWUC7JLBEQAVQSE"
    get_single_weather_list = get_single_weather(key,"metric","datetime,datetimeEpoch,name,address,resolvedAddress,latitude,longitude,temp,humidity,precip,solarradiation,solarenergy,stations,source","obs,days","json")
    data = json.loads(get_single_weather_list)
    print(json.dumps(data["days"]))
    print(json.dumps(data["stations"]))

if __name__ == "__main__":
    main()
