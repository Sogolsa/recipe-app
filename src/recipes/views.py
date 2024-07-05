from django.shortcuts import render


# Create your views here.
def home(request):
    """takes the request coming from the web application and returns
    the template available at recipes/home.html as a response."""
    return render(request, "recipes/recipes_home.html")
