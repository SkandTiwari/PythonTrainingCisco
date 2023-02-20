from flask import Flask, request, jsonify

owelist = {
  "name": "Adam",
  "owes": {
    "Bob": 12.0,
    "Chuck": 4.0,
    "Dan": 9.5
  },
  "owed_by": {
    "Bob": 6.5,
    "Dan": 2.75,
  },
  "balance": "<(total owed by other users) - (total owed to other users)>"
}

ioutracker = Flask(__name__)

@ioutracker.get("/owelist", methods = ['GET'])
def get_list():
    return jsonify(owelist)

if __name__ == "__main__":
    ioutracker.run(debug=True)