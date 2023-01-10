from django.shortcuts import render
from .forms import UserForm
from django.views.generic import CreateView
from django.contrib.auth.models import User

# Create your views here.
class UserCreateView(CreateView):
	model = User
	form_class = UserForm
	template_name = "register.html"
