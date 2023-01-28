import requests

path = 'https://api.api-ninjas.com/v1/exercises'



query_params = {
  "type": "strength",
  "muscle": "chest"
}

response = requests.get(path, params=query_params, headers={'X-Api-Key': EXERCISE_API_KEY})

print("The value of the response is", response)
print("The value of response.text, which contains a text description of the request, is", response.text)