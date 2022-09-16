import requests

#   Numbers represent something:
#   1XX - Hold on
#   2XX - Here you go
#   3XX - Go Away
#   4XX - You screwed up
#   5XX - I screwed up

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()     # This line tells me what exception I am getting

data = response.json()      # response.json()["iss_position"] to get specific data key
print(data)

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
iss_pos = (longitude, latitude)
print(iss_pos)
