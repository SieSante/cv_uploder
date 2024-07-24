from django.urls import path
from .views import signup_view, login_view, upload_cv_view, profile_view, admin_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('upload_cv/', upload_cv_view, name='upload_cv'),
    path('profile/', profile_view, name='profile'),
    path('admin/', admin_view, name='admin'),
]
