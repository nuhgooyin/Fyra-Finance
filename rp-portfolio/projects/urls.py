from django.urls import path
from . import views

# List containing URL patterns
urlpatterns = [

    # Connecting root URL of app to the project_index view
    path("", views.project_index, name="project_index"),
    
    # <int:pk> notation dynamically generates primary keys which are then used in the URL
    path("<int:pk>/", views.project_detail, name="project_detail"),
]

# <int:pk> tells Django the value passed in the URL is an integer and the variable name is pk (primary key)