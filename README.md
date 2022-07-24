# Full Stack API Final Project


## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.


1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.


## Local Requirement
Requires Python 3.6 or Later

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

##### To Create a virtual Environment

```
python -m venv venv
```

##### To Start the environment for Windows Users
```using git bash
source venv/Script/activate
```
#### Backend Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```git bash (For Windows Users)
pip install -r requirements.txt
```

## Database Setup

#### Running Postgresql server on windows
To `start` your server use
`  pg_ctl -D "c:\Program Files\PostgreSQL\[Your PostgreSQL Version]\data" start
`
>Example (using git bash)
```git bash
 pg_ctl -D "c:\Program Files\PostgreSQL\13\data" start
```

To `Stop` your server use
`  pg_ctl -D "c:\Program Files\PostgreSQL\[Your PostgreSQL Version]\data" stop
`
>Example (using git bash)
```bash
 pg_ctl -D "c:\Program Files\PostgreSQL\13\data" stop
```
 
 Create a database called `trivia` using [psql](https://www.postgresql.org/docs/9.2/app-psql.html)

 ```
 CREATE DATABASE trivia;
 ```

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal(For Windows Users) run:
`psql -f database_file -U user database_name`

```bash
psql -f trivia.psql - U postgres trivia 
```
## Running the server

From within the `backend` directory first en sure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

## Setting up the Frontend

> Note: The frontend is design to work with endpoints in the backend -> [Flask-based Backend](../backend). It is recommended you set up the backend first, using Postman or curl to test the backend first, update the endpoints in the frontend, and every thing will work perfectly.

### Installing Frontend Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>Note : You can also use **npm i** it is shorthand for **npm install**

## Required Tasks

## Running Your Frontend

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

```bash
npm start
```

