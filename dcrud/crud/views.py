from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, RecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in.")
            return redirect('home')
        else:
            messages.warning(request, "There is an error. Try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})


def customer(request, pk):
    if request.user.is_authenticated:
        customer = Record.objects.get(id=pk)
        return render(request, 'customer.html', {'customer': customer})
    else:
        messages.warning(request, 'Invalid requiest.')
        return redirect('home')
    

def delete_customer(request, pk):
    if request.user.is_authenticated:
        customer = Record.objects.get(id=pk)
        customer.delete()
        messages.success(request, 'Customer deleted successfully.')
        return redirect('home')
    else:
        messages.warning(request, 'Invalid requiest.')
        return redirect('home')
    

def add_customer(request):
    form = RecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                customer = form.save()
                messages.success(request, 'Customer added successfully.')
                return redirect('home')
        return render(request, 'add_customer.html', {'form': form})
    else:
        messages.warning(request, 'You must login first.')
        return redirect('home')
    

def update_customer(request, pk):
    if request.user.is_authenticated:
        customer = Record.objects.get(id=pk)
        form = RecordForm(request.POST or None, instance=customer)
        if form.is_valid():
                form.save()
                messages.success(request, 'Customer updated successfully.')
                return redirect('home')
        return render(request, 'add_customer.html', {'form': form, 'customer': customer})
    else:
        messages.warning(request, 'You must login first.')
        return redirect('home')
        