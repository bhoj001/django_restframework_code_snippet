
from django.contrib import admin
from django.urls import path, include
from .routers import router
from rest_framework.authtoken import views

# This is for session authentication
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('snippets/', include('snippets.urls', namespace='snippets')),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api-auth-token/',views.obtain_auth_token, name='api-auth-token'),
    # below is new syntax for login views
    # path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]


