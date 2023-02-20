"""After playing around with fake APIs, its time to create our own APIs. We'll use REST API to accomplish this..."""
from flask import Flask, request, jsonify
api_url = "https://jsonplaceholder.typicode.com/todos/10"

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

"""place = {
    "area": 7617930,
    "capital": "Canberra",
    "id": 2,
    "name": "Australia"
}"""

@app.route('/')
def index():
    return "Your API will appear here"

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.get("/country")
def get_country():
    return countries[0]

if __name__ == "__main__":
    app.run(debug=True)


