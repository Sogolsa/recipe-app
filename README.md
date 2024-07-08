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

# Creating a Custom Welcome Page

1. Defining the view in the app/views.py file.
2. Creating the template(s) in the app/templates/ folder.
3. Mapping the URL to view in app/urls.py.
4. Registering the URL and view in project/urls.py.

## Defining View

- app/views.py: Specify the function => take a web request (as input) => return a web response.
- Web response can be anything—an HTML page, an image, or whatever response you choose to provide
- The important thing is to specify the file path that corresponds to the response, and to point exactly from where the response can be loaded

## Creating Templates:

1. Create a folder named templates within the app with defined view.
2. Within the templates folder, create a new folder that is named the same as the app.
3. Create the template pages as needed (recipes_app.html)
4. Specify the path to recipes/recipes_home.html in the views.py file.

## Map view to URL:

1. Create a urls.py file in app folder
2. Specify the path in app/urls.py => to connect to route corresponding to http://127.0.0.1:8000/ => with view specified by app/urls.py

```bash
from django.urls import path
from .views import home


app_name = "recipes"

urlpatterns = [path("", home)]
```

3. Update the urls.py file in your main recipe project by registering the view to urlpatterns.

```bash
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [path("admin/", admin.site.urls), path("", include("recipes.urls"))]
```

## Run Server

- Navigate to project/src
- Activate the virtual environment
- run the server: `python manage.py runserver`

# Accessing Records from the Database

1. Specifying all attributes in the Recipes model.
2. Entering recipes records in the database.
3. Creating the view and templates to display the list of recipes and registering the URLs with the app (recipes) and the project.

## Step 1: Specify Attributes in the Recipes Model

1. Have a designated folder where the images will be stored(media in src). This needs to be done once per project.
2. Specify the path to the folder in the project’s settings.py file. This also needs to be done once per project:

```bash
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

3. Specify URL-View mapping in the project’s urls.py file. This is a project-level entry and only needs to be done once per project.

```bash
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

4. (and 5): Update the code in the models.py files to create the attribute in the database. Also, provide the no_picture.jpg image by default. For this, add the following statement in your recipes/models.py file:

`pip install pillow`
`pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')`

- Activate virtual environment => run `python manage.py makemigrations` => `python manage.py migrate` => Run server
