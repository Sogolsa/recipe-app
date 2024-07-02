# Recipe App

Creating a recipe app using Django web framework. In this application PostgreSQL is used for the backend, HTML and CSS are used for the front end. And the app will be deployed on Heroku
The final application is dynamic and multi-user, letting users sign up, and create their own content. It also has statistical dashboards, implementing data analytics and data visualizations.

## Creating a Django Project Structure

Step 1:

- Create a new virtual environment: `mkvirtualenv a2-ve-recipeapp`
- Activate virtual environment: `Envs\a2-ve-recipeapp\Scripts\activate.bat` for windows

Step 2:

- Install Django: `python -m pip install Django`

- Create a project inside the A2_Recipe_App directory: `django-admin.exe startproject <project_name>`
- Rename the recipe_project to src: To rename => make sure you are outside root directory (recipe_project)=> `rename recipe_project src` for windows cmd

Step 3:

- From within src folder: run migrations, run server
- To run migrations: inside src folder => `python manage.py migrate`
- To run the server on windows: `python manage.py runserver`

Step 4:

- Create superuser to access the admin panel: In src folder: `python manage.py createsuperuser`

- leave user name blank => take default user name
- email address optional
- Create a password:

Step 5: run the server
`python manage.py runserver`

- Log in to the Django site admin in localhost.
  http://127.0.0.1:8000/admin/ => login

## Creating Apps

- For recipe app, I have recipe and users apps

### Create recipes app:

1. in src directory run: `python manage.py startapp recipes`
2. link the apps to the recipe_project application:
   update project's settings with the new app information
3. Navigate to main project folder => recipe_project => open settings.py
4. INSTALLED_APPS variable => extend the list by adding the apps
5. Now time to define and work with django models

# Django Models: Defining, Registering, Migrating, and Running (4 steps)

1. Defining the model:

- Navigate to the app and open models.py => define the class
- specify the string representation of the object

2. Register classes in admin.py:

```bash
from .models import <class name>
admin.site.register(<class name>)
```

3. Migrate the models to create tables:

- in src folder:
  `python manage.py makemigrations`
- Apply the changes to database:
  `python manage.py migrate`

4. Run the server:
   `python manage.py runserver`

The 'M' part of Django MVT is completed with these 4 steps.

# Writing Tests:

- test.py file => write test class:
  `from .models import <class name>`
  `class MyTestClass(TestCase):`
- Define the test cases as class methods within this class:

  1. setUpTestData: run before every test run, to initialize variables that will not change during the test execution.

  2. setUp: run before every test method to ensure that all variables that will change during test execution are correctly initialized.

  3. tearDown: clean-up run after every test method.

  4. test_something: one or more functions that return a True or False, based on assertions.

- Writing Test in test.py:
  `<model>.objects.create()` => pass it the initial values as an argument

## Run the test in src folder

`python manage.py test`

- To run all the tests found within the books app:
  `python manage.py test <app name>`
- To run just one test case (say, the test case BookModelTest under books app)
  `python manage.py test books.tests.BookModelTest`
- To run just one test method (say, the test for maximum length for author name under the BookModelTest test case)
  `python manage.py test books.tests.BookModelTest.test_author_name_max_length`

- Specify how many details you want to be displayed in terminal (--verbosity).
- Check if your tests are in files that don’t start with the name test (--pattern).
- Speed up testing by running tests in parallel (--parallel).

- check out the full list of available commands by typing `python manage.py test --help`
