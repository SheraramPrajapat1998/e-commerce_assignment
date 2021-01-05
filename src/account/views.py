from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm

def dashboard(reqeust):
  return render(request, 'account/dashboard.html')
  
def register(request):
  user_form = UserRegistrationForm()
  if request.method == 'POST':
    user_form = UserRegistrationForm(data=request.POST)
    if user_form.is_valid():
      new_user = user_form.save(commit=False)
      # save encrypted password instead of raw password
      new_user.set_password(user_form.cleaned_data['password'])
      new_user.save()
      return render(request, 'account/register_done.html', {'new_user':new_user})
  return render(request, 'account/register.html', {'user_form':user_form})
