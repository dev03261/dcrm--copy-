#Todo App README

EATURES OF PROJECT:

Sign Up:
To create your user account, you'll need to choose a username and a password. The username is like your nickname on the website, and the password is like a
secret code that only you should know. You'll also need to type the same password again to make sure you didn't make any mistakes.

Log In:
When you want to log into your account, you'll need to tell the website your username and your password. It's like telling your name and secret code to the
website so it knows it's really you.

Create Task:
If you want to add a new task to your list, you should provide some information about it. This information includes what the task is about, how important it is,
and whether you've finished it or not.

Edit Task:
If you need to change something about a task you already added, you can do that too. You just need to tell the website what you want to change. For example,
you can update what the task is about or how important it is.

Delete Task:
If you decide you don't want a task on your list anymore, you can remove it. There should be a little picture that looks like a trash can or delete icon.
Just click on that, and the task will disappear.


PREREQUISITS
Before you begin with this Todo App, make sure you have the following software installed on your machine:

    Python
    Django
    Docker
    Postman


POJECT SETUP
1. Clone the Repository
First, clone the repository to your local machine using the following command:
bash
git clone https://github.com/dev03261/todoApp.git
cd todo-app

2. Create a Virtual Environment (Optional but Recommended)
It's a good practice to work within a virtual environment to isolate your project's dependencies. To create and activate a virtual environment, use the following commands:
bash
python -m venv virt
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Project Dependencies
Install the required project dependencies by running the following command:
bash
pip install -r requirements.txt

4. Database Configuration
By default, this app uses SQLite as the database. However, you can configure other databases in the settings.py file if needed.
Migrations
Run the initial migrations to set up the database schema:
bash
python manage.py migrate

5. Running the App Locally
To run the app locally, use the following command:
bash
python manage.py runserver
The app will be accessible at http://127.0.0.1:8000/ in your web browser.

6. Dockerization
If you prefer to run the app in a Docker container, follow these steps:
Build the Docker Image
Build the Docker image using the following command:
bash
docker build -t todo-app .
Run the Docker Container
Start the Docker container with the following command:
bash
sudo docker-compose up
