from django.urls import path
from . import views
from home.views import login_request, logout_view, indexAccountView, account_address_delete, DeleteEvent, \
    RegisterUserEvent, DeleteUserEvent

app_name = 'home'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # Manage users
    path('login/', login_request, name="login"),
    path('logout/', logout_view, name="logout"),
    path('sign-up/', views.SignUpView.as_view(), name='signup'),
    path('account/', indexAccountView, name='account'),
    path('account/reservation/<int:pk>/', views.UserEventDetails.as_view(), name="reservation-detail"),

    # Manage schools
    path('schools/', views.SchoolIndexView.as_view(), name="schools"),
    path('school/create', views.CreateSchoolView.as_view(), name="school-create"),
    path('school/<str:id>/', views.SchoolDetailsView.as_view(), name="school-details"),
    path('schools/<int:pk>/delete/', account_address_delete, name='school-delete'),
    path('schools/slots-available/', views.SchoolsWithReservationsOnly.as_view(), name="schools-with-slots"),

    # Manage events
    path('school/<int:pk>/add-event/', views.ManageEventView.as_view(), name="add-event"),
    path('school/<int:pk>/edit/<int:pk2>', views.ManageEventView.as_view(), name="edit-event"),  # TO modify
    path('school/event/<int:pk>/delete', DeleteEvent, name="delete-event"),

    # Manage users actions
    path('pick-slot/<int:id>', RegisterUserEvent, name="pick-slot"),
    path('cancel-slot/<int:id>', DeleteUserEvent, name="cancel-slot"),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
