from django.shortcuts import render
from django.shortcuts import render_to_response, RequestContext

from .models import User
from .forms import UserForm

# Create your views here.

def home(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		new_join.save()
	return render_to_response('/static/template/user/home.html', locals(), context_instance=RequestContext(request))

