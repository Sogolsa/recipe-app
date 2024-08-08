from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  # Django authentication libraries
from django.contrib.auth.forms import (
    AuthenticationForm,
)  # Django Form for authentication


def login_view(request):
    """Function based view that takes a request from user and initialized error message"""
    error_message = None

    # Create a form object of class authentication
    form = AuthenticationForm()

    # When user hits login button, POST request is generated
    if request.method == "POST":
        # read the data sent by the form via POST request
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            """Check if form is valid"""
            username = form.cleaned_data.get("username")  # Read username
            password = form.cleaned_data.get("password")  # Read password

            # use Django authenticate function to validate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                """If the use is authenticated, use pre-defined django function to login, 
                and send the user to desired page"""
                login(request, user)
                return redirect('recipes:recipes')
        else:
            error_message = "Oops.. something went wrong"


    # prepare data to send from view to template, send the form data and the error message
    context={"form":form, "error_message":error_message}
    
    # Load the login page using "context" information
    return render(request, "auth/login.html", context)


def logout_view(request):
    """Take the request from user"""
    logout(request)
    return render(request, "auth/success.html")

            
            
        
