# Casting-Agency-Specifications

## Motivation for project
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

Models:

Movies with attributes title and release date
Actors with attributes name, age and gender
Endpoints:
GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/
Roles:
Casting Assistant
Can view actors and movies
Casting Director
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies
Executive Producer
All permissions a Casting Director has and…
Add or delete a movie from the database
Tests:
One test for success behavior of each endpoint
One test for error behavior of each endpoint
At least two tests of RBAC for each role

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

```bash
pip install virtualenv
virtualenv --no-site-packages env
source env/bin/activate
```

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
When testing locally, models.py should be:
```python
# database_path = os.environ['DATABASE_URL']

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

# db = SQLAlchemy()
```
When testing on heroku, models.py should be:
```python
database_path = os.environ['DATABASE_URL']

# database_filename = "database.db"
# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()
```

From the working folder in terminal run:
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## Running the server locally

To run the server, execute:

```bash
python app.py
```

## Running the server on heroku

I have already deployed the API in heroku and can use it directly. The host is:

https://casting-agency-fxzero.herokuapp.com/movie

You can test the API like this:

```bash
curl -H "Authorization: Bearer ${TOKEN}" https://casting-agency-fxzero.herokuapp.com/movies | jq 
```

## API document
```
Endpoints
GET '/actors'
POST '/actors'
PATCH '/actors/<actor_id>'
DELETE '/actors/<actor_id>'
GET '/movies'
POST '/movies'
PATCH '/movies/<movie_id>'
DELETE '/movies/<movie_id>'


GET '/actors'
- Get all actors' information
- Request Arguments: None
- Returns: A list contains all the actors' info.


POST '/actors'
- Add a actor

PATCH '/actors/<actor_id>'
- Update a actor's information

DELETE '/actors/<actor_id>'
- Delete a actor
- Request Arguments: actor_id
- Returns: The id of the actor which was deleted 
{
  "actors": "1",
  "success": true
}

GET '/movies'
- Get all movies' information
- Request Arguments: None
- Returns: A list contains all the movies' info.

POST '/movies'
- Add a movie

PATCH '/movies/<movie_id>'
- Update a movie's information

DELETE '/movies/<movie_id>'
- Delete a movie
- Request Arguments: movie_id
- Returns: The id of the movie which was deleted 
{
  "movies": "1",
  "success": true
}




GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

GET '/questions'
- Fetches a list of questions in which contain the info of each question
- Request Arguments: page
- Returns: An object with a list of questions, that contains a object of key:value pairs. 
{
  "categories": {
    "1": "science",
    "2": "art",
    "3": "geography",
    "4": "history",
    "5": "entertainment",
    "6": "sports"
  },
  "current_category": 3,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }
  ],
  "success": true,
  "total_questions": 20
}

DELETE '/questions/<question_id>'
- Delete a question
- Request Arguments: question_id
- Returns: The id of the question which was deleted 
{
  "deleted": "25",
  "success": true
}

POST '/questions'
- Create a new question, which will require the question and answer text, category, and difficulty score.
- Request Arguments: question, answer, category, difficulty
{
    "question":"new question!",
    "answer":"new answer!",
    "difficulty":"4",
    "category":"3"
}
- Returns: The id of the question which was added 
{
  "created": "25",
  "success": true
}

POST '/questions/s'
- get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
- Request Arguments: searchTerm
{
    "searchTerm":"Mirrors"
}
- Returns: A questions' list contaions the questions which match the search term
{
  "currentCategory": 3,
  "questions": [
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "totalQuestions": 1
}

GET '/categories/<category_id>/questions'
- Fetches a list of questions in which contain the info of each question that in specified category
- Request Arguments: category_id
- Returns: An object with a list of questions, that contains a object of key:value pairs. 
{
  "current_category": "1",
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    }
  ],
  "success": true,
  "total_questions": 3
}

POST '/quizzes'
- This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
- Request Arguments: previous_questions, quiz_category
{
    "previous_questions":[22],
    "quiz_category":{"type":"science","id":"1"}
}
- Returns: An object with a question, that contains a object of key:value pairs. 
{
  "question": {
    "answer": "Alexander Fleming", 
    "category": 1, 
    "difficulty": 3, 
    "id": 21, 
    "question": "Who discovered penicillin?"
  }, 
  "success": true
}
```


## Testing
To run the tests, run
```
pytest test_app.py
```

