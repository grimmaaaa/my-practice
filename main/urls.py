from django.urls import path

from .views import login_view, logout_view, MainView, register, UserUpdateView, WeaponApplicationView, PlacesView, BookView


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('profile/', UserUpdateView.as_view(), name='user_page'),
    path('weapon-application/', WeaponApplicationView.as_view(), name='application'),
    path('places/<str:location>/', PlacesView.as_view(), name='places'),
    path('book-place/<int:pk>/', BookView.as_view(), name='book'),
    path('', MainView.as_view(), name='home'),
]

app_name = 'main'
