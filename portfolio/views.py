from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Project 

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, "portfolio/home.html", {"projects":projects})
