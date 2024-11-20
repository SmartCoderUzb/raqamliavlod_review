from django.urls import path

from .views import signup_view, login_view, logout_view, profile


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('profile/', profile, name='profile')
]
