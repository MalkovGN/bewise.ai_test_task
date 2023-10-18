import os

from fastapi import FastAPI, Body
from fastapi_sqlalchemy import DBSessionMiddleware, db

from db import models
from app.utils import get_questions


app = FastAPI()

db_url = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASS']}@{os.environ['DB_HOST']}/{os.environ['DB_NAME']}"
app.add_middleware(DBSessionMiddleware, db_url=db_url)


@app.post('/question_numbers')
def question_numbers(question_number: dict[str, int] = Body()):
    last_saved_question = db.session.query(models.Question).all()
    if not last_saved_question:
        last_saved_question = {}
    else:
        last_saved_question = last_saved_question[-1]

    number_of_questions = question_number['questions_num']
    questions = get_questions(number_of_questions)
    same_questions = 0
    while number_of_questions != 0:
        for question in questions:
            check_db_question = db.session.query(models.Question).filter(models.Question.id == question['id']).first()
            if not check_db_question:
                db_question = models.Question(
                    id=question['id'],
                    question_text=question['question'],
                    answer_text=question['answer'],
                    created_at=question['created_at']
                )
                db.session.add(db_question)
                number_of_questions -= 1
            else:
                same_questions += 1
        questions = get_questions(same_questions)
        db.session.commit()
    return {
        'id': last_saved_question.id,
        'question_text': last_saved_question.question_text,
        'answer_text': last_saved_question.answer_text,
        'created_at': last_saved_question.created_at
    } if last_saved_question != {} else {}
