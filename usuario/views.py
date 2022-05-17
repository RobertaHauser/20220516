from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Usuario

# Create your views here.
def index(request):
    return render(request,'index.html')


class UsuarioCreate(CreateView):
    template_name="form.html"
    model=Usuario
    fields=['email','password']