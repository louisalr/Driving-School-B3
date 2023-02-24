from django.urls import path
from . import views
from home.views import login_request, logout_view, indexAccountView

app_name = 'home'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sign-up/', views.SignUpView.as_view(), name='signup'),
    path('login/', login_request, name="login"),
    path('logout/', logout_view, name="logout"),
    path('schools/', views.SchoolIndexView.as_view(), name="schools"),
    path('school/<str:id>/', views.SchoolDetailsView.as_view(), name="school-reservations"),
    path('account/', indexAccountView, name='account'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
