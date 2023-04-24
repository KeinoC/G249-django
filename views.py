from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, authenticate, login
from django.http import HttpResponse
from models import User


def my_view_function(request):
    # Handle GET request
    if request.method == 'GET':
        # Retrieve data from your database or other sources
        # Process the data as needed
        # Return an HttpResponse with the data
        return HttpResponse('Hello, this is a GET request.')

    # Handle POST request
    elif request.method == 'POST':
        # Retrieve data from the request's POST data
        posted_data = request.POST.get('data')  # Example: assuming data is passed as a form field called 'data'
        # Process the data as needed
        # Save the data to your database or other storage
        # Return an appropriate response, e.g., a success message
        return HttpResponse('Data has been saved successfully: {}'.format(posted_data))

    # Handle other HTTP methods as needed
    else:
        # Return an appropriate response for other methods
        return HttpResponse('Method not allowed.', status=405)
    

def users(request):
# Handle GET request
    if request.method == 'GET':
    # Retrieve user data from your database or other sources
    # Process the data as needed
    # Return an HttpResponse with the user data
        return HttpResponse('Hello, this is the users endpoint for GET request.')

# Handle POST request
    elif request.method == 'POST':
    # Retrieve user data from the request's POST data
        posted_data = request.POST
        username = posted_data.get('username')
        password = posted_data.get('password')

    # Hash the user password
        hashed_password = make_password(password)

    # Save the user data to your database or other storage
    # Note: You should also perform additional validation and error handling here
    # before saving the user data to the database

    # Example: Saving user data to a hypothetical User model
        user = User(username=username, password=hashed_password)
        user.save()

    # Return an appropriate response, e.g., a success message
        return HttpResponse('User data has been saved successfully.')

# Handle other HTTP methods as needed
    else:
    # Return an appropriate response for other methods
        return HttpResponse('Method not allowed.', status=405)


####################

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # User credentials are valid, login the user
            login(request, user)
            return HttpResponse('Login successful')
        else:
            # User credentials are invalid, return an error response
            return HttpResponse('Invalid username or password')
    else:
        # Handle GET request as needed
        return HttpResponse('Hello, this is the login endpoint for GET request.')