import requests

parameters = {
    "amount": 10,
    "difficulty": "easy",
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean", params=parameters)#you can change theme of quiz by going to the trivia website
response.raise_for_status()

question_data = response.json()["results"]
