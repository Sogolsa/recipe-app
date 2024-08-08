# Recipe App

Creating a recipe app using Django web framework. In this application PostgreSQL is used for the backend, HTML and CSS are used for the front end. And the app will be deployed on Heroku
The final application is dynamic and multi-user, letting users sign up, and create their own content. It also has statistical dashboards, implementing data analytics and data visualizations.

# Dependencies used in Production

- whitenoise==6.7.0
- dj-database-url==2.2.0
- gunicorn==22.0.0
- psycopg2==2.9.9

# Set up the app

bash```

1. git clone <repository-url>`
2. cd recipe-app
3. pip install -r requirements-dev.txt: install development dependencies.
4. configure the settings: SECRET_KEY, DEBUG, DATABASES
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py runserver

````
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
````

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

## Step 2: Add Recipes (Records) in the Database

- In the admin panel click add and add records

## Step 3: Specify View, Create Template, and Register URL

- Data is now in the database at the backend of Recipes application.
- For Front end: 4 step process:

1. Specify the View: recipes/views.py

- Import Django's ListView package (display data as a list)
- Import the Recipes Model(provides access to recipe records)
- Create a class based view(custom logic is not needed, generic functionality is good enough) => specify the model and template

2. Create Template:

- template is an HTML file that should be created in the recipes/templates/recipes folder
- create the recipe list first by accessing the model. Then, you’ll turn toward formatting and tabling.
- when the view executes, the model’s records are stored as a list in the variable called object_list(built-in variable)
- To access individual records within the object_list => loop through the list (for loop in recipes_list.html)
- Once you register your URL, you’ll be able to see your list of recipes
- Access recipe title and images: by {{object.name}} {{object.pic}}
- Specify the path to the image file (using {{object.pic.url}}) and then use the HTML image tag <img> to show the image

```bash
{% for object in object_list %}
   {{object.name}} - <img src="{{object.pic.url}}" width="150" height="200" />
   <br>
{% endfor %}
```

3. Map view to URL:

- create a new file: recipes/urls.py.
- To connect list/ with the RecipeListView (a class-based view), you need to call as_view() (a method of class ListView), which returns a callable view that takes a request and returns a response. as_view() => not needed for function based view

`urlpatterns = [path("recipes/", RecipeListView.as_view(), name="recipes")]`

4. Registering the View:

- recipe_project/urls.py

```bash
urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('recipes.urls')),
]
```

# Login and Authentication (4 Step Process)

- Login form for recipe_project application (reached at “http://127.0.0.1:8000/login/”)
- The 4 steps will be created under the recipe_project

1. Create the view
2. Create the template
3. Specify the URL mapping
4. Register the URL to the project

## Step1: Create the View

- In recipe_project folder => Create a new file => views.py
- Create a new function based view login_view (login form based on django's authentication form)
- Import Django's authentication libraries, and form for authentication:
  `from django.contrib.auth import authenticate, login`
  `from django.contrib.auth.forms import AuthenticationForm`

- when user hits "login" button, then POST request is generated
- read the data sent by the form via POST request
- check if form is valid
- use Django authenticate function to validate the user
- then use pre-defined Django function to login

## Step 2: Create the Template:

- Under src: create folder => templates => create folder => auth => create file => login.html
- Since this template is outside apps (new location) => tell django to look elsewhere for templates:
- recipe_project/settings.py => scroll down to TEMPLATES list variable
- Update DIRS list to: `'DIRS': [BASE_DIR / 'templates'],`
- Save settings.py

## Step 3: Specify the URL Mapping:

- Since you are not coding within an app, skip this step and head over to project level urls.py

## Step 4: Register the URL to the Project:

- recipes_project/urls.py: import login_view from the views:
  `from .views import login_view`
- Include the login_view path in urlpatterns

```bash
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("recipes.urls")),
    path("", include("users.urls")),
    path('login/', login_view, name='login'),
]
```

# Protecting Views

- If you try to load the recipes list page without being logged in, Django will take you to the authentication form specified by LOGIN_URL in recipes/settings.py
- recipe_project/settings.py => towards the end of the script => add:

```bash
# Auth
LOGIN_URL='/login/'
```

- Navigate to the view to protect

## Protecting a Class-Based View (CBV)

- recipes/views.py:

```bash
from django.contrib.auth.mixins import LoginRequiredMixin
class RecipeListView(LoginRequiredMixin, ListView):
    """Class based view"""

    model = Recipe  # Specify model
    template_name = "recipes/recipes_list.html"  # Specify template
```

## Protecting a Function-Based View (FBV)

- recipes/records:

```bash
#to protect function-based views
from django.contrib.auth.decorators import login_required
#keep protected
@login_required
def profile(request):
    user = User.objects.first()
    context = {"user": user}
    return render(request, "users/user_profile.html", context)
```

# Implement Logout

- Create the view
- Register the view
- recipe_project/views.py: `from django.contrib.auth import logout`
- Define a function based logout_view
- Logout view doesn't need template => proceed to registering the URL to projects urls.py
- Register URL to project's urls.py:

```bash
from .views import logout_view

urlpatterns = [
   ...
   path('logout/', logout_view, name='logout'),
]
```

# Data Analysis and Visualization in Django

## Search For Records

1. Take input from user via form.
2. Display search records in a table.
3. Display chart.

### 1: Creating a User-Input Form (3 Step Process)

#### Step 1: Create a form named recipes/forms.py

- This will be to specify the search form fields
- Create a new file named forms.py in recipe folder.
- Import forms from Django:
  `from django import forms`
- Specify the fields that you want in your search form.
  In recipes app => specify chart choices then => define the class based form: RecipesSearchForm
- Import the RecipesSearchForm to the view for user input

#### Step 2: Update view in recipes/views.py

- Import the form you created in recipes/forms.py:
  `from .forms import RecipesSearchForm`
- Define function based view search_recipes that takes the request
- Prepare the context dictionary to pass parameters from view to template.
- Finally, send the request and context to the template recipes/recipes_list.html

#### Step 3: Update recipes_list.html template in recipes/templates/recipes

- Start by specifying a heading for the page
- Include the form, using {{form}} that was sent from the view through the context dictionary (which was prepared in Step 2).
- A button called search will be created with the “submit” form functionality
- {% csrf_token %} => CSRF stands for Cross Site Request Forgery protection, which is a Django security feature

# Implementing Search Functionality and Displaying Search Records

- recipes/views.py file => implement search functionality.

## Step 1: Read data entered into the form by the user.

- recipes/views.py => check if form button is clicked (the request is made)
- If true => read data from form

## Step 2: Extract data from the database using QuerySet API.

- QuerySet is an API used to provide access to data present in the database.
- In recipes/views.py => `from .models import Recipe` => since we access the recipes data

## Step 3: Convert QuerySet to pandas DataFrames to make data available for further processing.

- pandas => python library => provides fast and efficient data analysis
- DataFrame => 2 dimensional data structure => data stored in tabular form in rows and columns

### Install pandas:

- In terminal
- Activate virtual environment
- `pip install pandas`
- Return to recipes/views.py
  `import pandas as pd`
- Next, initialize a DataFrame object as None in search_recipes()
  `recipes_df=None`
- Use the filter function to extract the desired results as a QuerySet.
- Check if there’s any data matching the criteria, and if there is, then convert the QuerySet to a pandas DataFrame.
  `recipes_df=pd.DataFrame(qs.values())`
- At the end of search_recipes() function, update your context dictionary to send the recipes_df DataFrame to the recipes/recipes_list.html template.

# Data Visualization

- install matplotlib `pip install matplotlib`

## Update recipes/utils.py to implement charting functions

- Create a file-like object BytesIO (python method to manipulate binary data) and matplotlib

```bash
from io import BytesIO
import base64  # Encode and Decode method on object
import matplotlib.pyplot as plt
```

- Start implementing getgraph() => take care of low level image handling details =>done once per project
- getgraph() function needs to be called by another function => getchart()
- getchart() => implements the logic to prepare the chart based on user input => and calls getgraph() to generate the chart at file/byte level.

- Next => recipes/views.py => call getchart():
