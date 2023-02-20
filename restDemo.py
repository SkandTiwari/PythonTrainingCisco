"""In this tutorial we'll create REST APIs, We'll use fake API Endpoints for the testing purpose. The sole objective of this test is to lay a strong backend-development skill"""


import requests

# api_url = "https://jsonplaceholder.typicode.com/todos" # Updated for post request
api_url = "https://jsonplaceholder.typicode.com/todos/10"

#=============================================================================================
# GET Request Demo

"""response = requests.get(api_url) # Getting the response

temp = response.json() # Coverting into JSON format

print("Content data : ", response.headers["Content-Type"]) # printing content type



print("Status-Code : ", response.status_code)
# printing the status code


print("Requested data : ", temp)"""

# printing the final data

#=============================================================================================
# POST Request

todo_data = {
    "userId": 1,
    "title": "Make chai",
    "completed": False
}

"""response = requests.post(api_url, json = todo_data)

print("JSON Response after POST REQ : ",response.json())
print("Status-Code : ", response.status_code)"""

#=============================================================================================
# PUT Request Demo

"""response = requests.get(api_url)
print("Data before using PUT : ", response.json())

response = requests.put(api_url, json = todo_data)
print("Data after PUT : ", response.json())
print("Status-Code : ", response.status_code)
"""

#==============================================================================================
#PATCH Request

todo_updt = {"title" : "make coffee!"}
response = requests.patch(api_url, todo_updt)
print("Response : ", response.json())