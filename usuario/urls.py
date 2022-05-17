from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, index


urlpatterns = [
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(
            template_name='login.html'
        ), name="login"),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),

]