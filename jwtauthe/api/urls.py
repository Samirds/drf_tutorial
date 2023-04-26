from django.urls import path, include
from api.views import Registration
from .views import Login


urlpatterns = [
    path('register/', Registration.as_view()),
    path('login/', Login.as_view())
    
   
]
