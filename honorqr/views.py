from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Use get to avoid KeyError
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard page
        else:
            # Handle invalid login (e.g., show an error message)
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
