from django.shortcuts import render, redirect,get_object_or_404
from .forms import NewUserForm,ServiceForm,RentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Service, Rent

def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request,"Invalid username or password.")
    return render(request=request, template_name="myserviceapp/login.html")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
        	user = form.save(commit=False)
        	user.username = user.email
        	user = form.save()
       		login(request, user)
        	return redirect("home")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    return render (request=request, template_name="myserviceapp/register.html", context={"register_form":form})

def logout_request(request):
    messages_storage = messages.get_messages(request)
    for message in messages_storage:
        pass  # This will clear all messages
    logout(request)
    return redirect("login")

@login_required
def home(request):
    services = Service.objects.all()
    return render(request, 'myserviceapp/home.html', {'services': services})

@login_required
def service_detail(request, id):
    service = Service.objects.get(id=id)
    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            rent = Rent.objects.create(
                user=request.user,
                service=service,
                amount=amount
            )
            
            return redirect('service_detail', id=service.id)
    else:
        form = RentForm()
    service = get_object_or_404(Service, id=id)
    rents = service.rent_set.all()
    return render(request, 'myserviceapp/service_detail.html', {'service': service, 'rents': rents,'form':form})

@login_required
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.user = request.user
            service.save()
            messages.success(request, "New service added successfully.")
            return redirect('add_service')
    else:
        form = ServiceForm()
    return render(request, 'myserviceapp/add_service.html', {'form': form})

@login_required
def service_update(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, "Service updated successfully.")
            return redirect('service_update', service_id=service_id)
    else:
        form = ServiceForm(instance=service)

    return render(request, 'myserviceapp/service_update.html', {'form': form})