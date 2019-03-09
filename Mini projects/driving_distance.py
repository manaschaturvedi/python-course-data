import json
import requests

source_address = 'malad station west'
destination_address = 'try catch classes'
key = '' # insert your API key here
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins='+source_address+'&destinations='+destination_address+'&mode=driving&sensor=false&format=json&key=' + key
ans = requests.get(url)
j_ans = json.loads(ans.text)
distance = j_ans['rows'][0]['elements'][0]['distance']['text']

print('The driving distance is:',distance)