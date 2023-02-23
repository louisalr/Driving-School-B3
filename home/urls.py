from django.urls import path
from . import views
from home.views import login_request

app_name = 'home'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sign-up/', views.SignUpView.as_view(), name="signup"),
    path('login/', login_request, name="login"),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
