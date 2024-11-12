# djangoproject/views.py

from django.shortcuts import render, redirect
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = PostForm()
    
    return render(request, '/home/aymen/django-test/djangoproject/templates/djangoproject/create_post.html', {'form': form})

def success(request):
    return render(request, '/home/aymen/django-test/djangoproject/templates/djangoproject/success.html')

