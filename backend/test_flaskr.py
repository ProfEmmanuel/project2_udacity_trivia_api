import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format('postgres', 'password','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
                'question': 'The Astronomical Unit (AU) is a unit of measurement based on the average distance between what two bodies?',
                'answer': 'The Earth and the Sun',
                'category': 1,
                'difficulty': 5,
            }
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    # paginated_questions
     def test_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(len(data['questions']))

    def test_404_paginated_questions(self):
        res = self.client().get('/questions?page=100', json={'category': 1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # Testing deletion
    def test_delete_question(self):
        res = self.client().delete('/questions/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 2)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_422_if_question_to_delete_does_not_exist(self):
        res = self.client().delete('/questions/100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # Testing categories
    def test_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(len(data['categories']))

    def test_questions_by_categories(self):
        res = self.client().get('categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['categories'])

    def test_404_questions_by_categories(self):
        res = self.client().get('categories/100/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # Testing the add route on the frontend
    def test_question(self):
        res = self.client().post('/questions', json=self.new_question)
        self.assertTrue(res.status_code, 200)

        data = json.loads(res.data)
        self.assertTrue(data['success'])

    def test_search_question(self):
        res = self.client().post('/questions', json={'searchTerm': 'question'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['questions'])
        self.assertEqual(len(data['questions']), 10)

    # Testing the quiz route
    def test_quiz(self):
        res = self.client().post('/quiz',
                                 json={'previous_questions': [],
                                       'quiz_category':
                                       {'id': '1', 'type': 'Science'}})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['question'])
        self.assertEqual(data['question']['category'], 1)

    def test_422_quiz(self):
        res = self.client().post('/quiz',
                                 json={
                                     'previous_questions': []
                                 })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()