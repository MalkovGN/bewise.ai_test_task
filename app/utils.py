import requests


def get_questions(number_of_questions):
    url = f'https://jservice.io/api/random?count={number_of_questions}'
    questions = requests.get(url=url).json()
    return questions
