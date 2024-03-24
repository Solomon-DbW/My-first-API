import requests

response = requests.get('https://randomuser.me/api')

print(response.status_code) #200 = Successful connection
# print(response.json())

gender = response.json()['results'][0]['gender'] # Gets the value of the gender
print(gender)

title = response.json()['results'][0]['name']['title']

first_name = response.json()['results'][0]['name']['first'] # Gets the value of the first name

last_name = response.json()['results'][0]['name']['last']

age = response.json()['results'][0]['dob']['age'] # Gets the value of the age
print(title,first_name,last_name)
print(f"Age = {age}")

