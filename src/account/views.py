from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ProfileEditForm, UserEditForm, UserRegistrationForm

@login_required
def dashboard(request):
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

@login_required
def edit(request):
  if request.method == 'POST':
    user_form = UserEditForm(data=request.POST, instance=request.user)
    profile_form = ProfileEditForm(data=request.POST, instance=request.user.profile, files=request.FILES)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, 'Profile updated successfully')
    else:
      messages.error(request, 'Error updating your profile')
  else:
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
  context = {'user_form':user_form, 'profile_form':profile_form}
  return render(request, 'account/edit.html', context)