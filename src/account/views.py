from django.shortcuts import render

from django.contrib.auth.decorators import login_required

def dashboard(reqeust):
  return render(request, 'account/dashboard.html')
  