from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.forms  import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm



def register(request):
	if request.method=='POST':

		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Account Created for {username}!')
			return redirect('blog-home')
	else:
		form = UserCreationForm()

	return render(request,'users/register.html',{'form':form})

	
# messages.debug()
# messages.info()
# messages.success()
# messages.warning()
# messages.error()